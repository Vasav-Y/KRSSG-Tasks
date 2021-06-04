#!/usr/bin/env python
#!/usr/bin/env python
import socket
import pickle
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt
import cv2

size = []
img = cv2.imread("Images/img2.png")
size.append(img.shape[0])
size.append(img.shape[1])


PI = 3.1415926535897
scale = 11.088889

xvals = []
yvals = []

class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.callback)

        self.pose = Pose()
        self.rate = rospy.Rate(10)
        self.linear_error = None
        self.angular_error = None
        self.linear_Integral = 0
        self.angular_Integral = 0

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        xval = goal_pose.x - self.pose.x
        yval = goal_pose.y - self.pose.y
        return sqrt(xval**2 + yval**2)

    def linear_vel(self, goal_pose, Kp =1.5 ,Ki = 0.0003, Kd = 1.0 , dt = 1, Imax = 0.02):
        if(self.linear_error == None):
            previous_error = self.euclidean_distance(goal_pose)
        else:
            previous_error = self.linear_error
        self.linear_error = self.euclidean_distance(goal_pose)
        P = Kp*self.linear_error

        if (self.linear_Integral  <Imax):
            self.linear_Integral  = self.linear_Integral  +Ki*self.linear_error
        else:
            self.linear_Integral =Imax

        D = Kd*((self.linear_error -previous_error)/dt)

        Ouput = P + self.linear_Integral + D
        return Ouput

    def steering_angle(self, goal_pose):
    
        return  (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x))

    def angular_vel(self, goal_pose, Kp = 3.000 , Ki = 0.0003, Kd = 1.0 , dt = 1, Imax = 0.002):
        if(self.angular_error == None):
            previous_error = (self.steering_angle(goal_pose) - self.pose.theta)
        else:
            previous_error = self.angular_error
        self.angular_error = (self.steering_angle(goal_pose) - self.pose.theta)

        P = Kp*self.angular_error

        if self.angular_Integral <Imax:
            self.angular_Integral =self.angular_Integral  +Ki*self.angular_error
        else:
            self.angular_Integral =Imax
        D = Kd*((self.angular_error-previous_error)/dt)

        Output = P + self.angular_Integral + D
        return Output
    

    def move2goal(self):
        """Moves the turtle to the goal."""
        goal_pose = Pose()
        for flag in range (0, len(Path)):

            goal_pose.x = xvals[flag]
            goal_pose.y = yvals[flag]

            distance_tolerance = 0.1
            angular_tolerance = 0.005

            vel_msg = Twist()

            while (abs(self.steering_angle(goal_pose)- self.pose.theta) >= angular_tolerance):

                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
            
                        # Angular velocity in the z-axis.
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)

                    # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)
                
            
                        # Publish at the desired rate.
                self.rate.sleep()

            # Stopping our robot after the movement is over.
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)

            while self.euclidean_distance(goal_pose) >= float(distance_tolerance):

                vel_msg.linear.x = self.linear_vel(goal_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                #angular velocity in the z-axis:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0

                # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)

                # Publish at the desired rate.
                self.rate.sleep()


        # If we press control + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        global Path
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((socket.gethostname(), 1237))
        Path = pickle.loads(c.recv(500))
        print(Path)

        Path.sort()
        for p in Path:
            m = (p[0]*scale)/size[1]
            xvals.append(m)
            n = ((size[0] - p[1])*scale)/size[0]
            yvals.append(n)

        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass




