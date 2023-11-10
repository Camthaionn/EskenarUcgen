#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import datetime
import time

rospy.init_node("duz_git")
pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
rate = rospy.Rate(10)
hiz_mesaji = Twist()

while not rospy.is_shutdown() :


			hiz_mesaji.linear.x = 0.1
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(10)
			#1.köşe
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 1
			pub.publish(hiz_mesaji)
			time.sleep(2.9999999)
			
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(2)
			
			#2.kenar
			hiz_mesaji.linear.x = 0.1
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(10)
			
			
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(2)
			
			
			#2.köşe
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 1
			pub.publish(hiz_mesaji)
			time.sleep(2.9999999)
			
			
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(2)
			
			#3.kenar
			hiz_mesaji.linear.x = 0.1
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(10)
			
			
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(2)
		
			#3.köşe
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 1
			pub.publish(hiz_mesaji)
			time.sleep(2.9999999)
			
			
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(2)
			
			#4.kenar
			hiz_mesaji.linear.x = 0.1
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
			time.sleep(11)
			
			
		
			hiz_mesaji.linear.x = 0.0
			hiz_mesaji.angular.z = 0.0
			pub.publish(hiz_mesaji)
		
		
		
		############ KOD BİTİMİ UZUN SLEEP
	
			rospy.is_shutdown()