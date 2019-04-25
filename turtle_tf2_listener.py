#!/usr/bin/env python  
import rospy

import random
import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import time

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    #spawns turtle2 or "follower"
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    turtle_name = rospy.get_param('turtle', 'turtle2')
    spawner(4, 2, 0, turtle_name)

    #spawns turtleBall
    turtle_ball = rospy.get_param('turtle', 'turtleBall')
    spawner(random.randint(1,9), random.randint(1,9), 0, turtle_ball)

    #initializes Publishers
    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)

    turtle_vel2 = rospy.Publisher('%s/cmd_vel' % turtle_ball, geometry_msgs.msg.Twist, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        #lookups initial transforms used to determine everythings relative position to one another
        try:
            trans = tfBuffer.lookup_transform(turtle_name, turtle_ball, rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        try:
            trans2 = tfBuffer.lookup_transform(turtle_ball, 'turtle1', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        try:
            trans3 = tfBuffer.lookup_transform(turtle_ball, turtle_name, rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        #create messages
        msg = geometry_msgs.msg.Twist()

        msg2 = geometry_msgs.msg.Twist()
        msg3 = geometry_msgs.msg.Twist()
        no_move = geometry_msgs.msg.Twist()

        #setting some message values
        msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        msg.linear.x = 1

        #set values for message sent to stop a turtle
        no_move.angular.z = 0
        no_move.linear.x = 0

        #gets current angle of turtleBall relative to turtle1 
        angle2 = trans2.transform.rotation.z

        #gets current angle of turtleBall relative to turtle2/"follower"
        angle3 = trans.transform.rotation.z
        print(angle3)

        #sets the angular velocity for ball when hit so that it rotates to direction its moving
        msg2.angular.z = 7
        msg3.angular.z = 7

        #checks if ball is within 0.25 units of turtle1
        if(-0.25 < trans2.transform.translation.x < 0.25 and -0.25 < trans2.transform.translation.y < 0.25):
            turtle_vel.publish(no_move)

            #while relative angle of the ball to turtle1 is greater than 0.1, rotate ball
            while(angle2 > 0.1 or angle2 < -0.1):
                turtle_vel2.publish(msg3)
                time.sleep(.05)
                print("still here")
                try:
                    trans2 = tfBuffer.lookup_transform(turtle_ball, 'turtle1', rospy.Time())
                except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                    rate.sleep()
                    continue
                angle2 = trans2.transform.rotation.z
                print(angle2)

            #sets angular velocity back to zero and moves straight
            msg2.linear.x = 3
            msg2.angular.z = 0

            turtle_vel.publish(msg)
            turtle_vel2.publish(msg2)
            print("still here 1")
            time.sleep(0.5)

        #checks if ball is within 0.25 units of turtle2
        if(-0.25 < trans.transform.translation.x < 0.25 and -0.25 < trans.transform.translation.y < 0.25):
            turtle_vel.publish(no_move)

            #while relative angle of the ball to turtle2 is greater than 0.1, rotate ball
            while(angle3 > 0.1 or angle3 < -0.1):
                turtle_vel2.publish(msg3)
                time.sleep(.05)
                print("still here")
                try:
                    trans = tfBuffer.lookup_transform(turtle_name, turtle_ball, rospy.Time())
                except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                    rate.sleep()
                    continue
                angle3 = trans.transform.rotation.z
                print(angle3)

            #sets angular velocity back to zero and moves straight
            msg3.linear.x = 3
            msg3.angular.z = 0

            turtle_vel.publish(msg)
            turtle_vel2.publish(msg3)
            print("still here 2")
            time.sleep(0.5)
            


        turtle_vel2.publish(no_move)
        turtle_vel.publish(msg)

        rate.sleep()
