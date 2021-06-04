#!/usr/bin/env python
#!/usr/bin/env python
from types import DynamicClassAttribute
from xmlrpc.client import escape
from rosgraph.names import anonymous_name
import rospy
from geometry_msgs.msg import Twist
from rospy.names import valid_name_validator_resolved
from turtlesim.msg import Pose
from math import atan2, sqrt


class TurtleBot:

    def __init__(self):
        #Creates a node with name 'turtlebot_controller' and make sure it is a 
        #unique node(using anonymous = True).
        rospy.inti_node('turtlebot_controller', anonymous = True)

        #Publisher whihc will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose' . self.update_pose is called
        # when a message of type Pose is recieved .
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()
        self.ratae = rospy.Rate(10)

    def update_pose(self, data):
        '''Callback function which is called when a new message of type Pose is 
        recieved by the Subscriber '''
        self.pose = data
        self.pose.x = round(self.pose.x ,4)
        self.pose.y = round(self.pose.y ,4)

    def euclidean_distance(self, goal_pose):
        '''Euclidean distance between current pose and the goal . '''
        xval = goal_pose.x - self.pose.x
        yval = goal_pose.y - self.pose.y

        return sqrt(xval**2 + yval**2)
    
    def linear_vel(self, goal_pose, constant = 1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
 
    def angular_vel(self, goal_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self):
        '''Moves the turtle to the goal.'''
        goal_pose = Pose()

        #Get the input from the user .
        goal_pose.x = float(input("Set your x coordinate of goal : "))
        goal_pose.y = float(input("Set your y coordinate of goal : "))

        #Please , insert a number slightly greater than 0 for eg( 0.01).

        distance_tolerance = float (input("Set your tolerance : "))

        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance :
            #Proportional Controller
             
            #Linear velocity in the x-axis
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #Angular velocity in the z axis
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(vel_msg)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            #Publishing at the desired rate.
            self.rate.sleep()

        #Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        #If we press control _ c, the node will stop
        rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException :
        pass
    

