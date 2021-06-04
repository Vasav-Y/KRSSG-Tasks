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

    def move2goal(self):
        """Moves the turtle to the goal."""
        goal_pose = Pose()
        for flag in range (0, len(Path)):

            goal_pose.x = xvals[flag]
            goal_pose.y = yvals[flag]

            distance_tolerance = 0.09
           
            vel_msg = Twist()

           
            while self.euclidean_distance(goal_pose) >= float(distance_tolerance):

                vel_msg.linear.x = 1.5 * self.euclidean_distance(goal_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                #angular velocity in the z-axis:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)

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




