"""
Class: Logger
Description: A class to pass ROS messages from one module to another.
			 ROS Messages can be written to textfile on disk based on a setting.

			 self._ROSflow:   Boolean value to indicate whether to log ROS messages to file.
			 				  True writes to file, False does not write to file.
			 				  Messages are published to subscribers regardless.

			 self._filename:  File on disk that will contain all messages passed with ROSflow set to true.

			 self._publisher: The publisher object that will publish data to the subscribers.
Author: Nishanth Hegde
Date: 10/10/2018
"""
class Logger():
	def __init__(self):
		self._ROSflow = False
		self._filename = "ROSlogs.txt"
		self._publisher = None

	def initPublisher(self, channel, dtype):
		self._publisher = rospy.Publisher(channel, dtype, queue_size = 10)

	def sendROSMessage(self, publisher, data):
		self._publisher.publish(data)
		if self._ROSflow:
			writeROSMessage(data)

	def writeROSMessage(self, filename, data):
		with open(self._filename, 'a') as output_file:
			write(data)

	def setROSflow(self, flow):
		self.ROSflow = flow

