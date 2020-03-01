#!usr/bin/env python

class Time(object):
	def __init__(self, h=0, m=0, s=0):
		self.hour = h
		self.minute = m
		self.second = s

	def later_than(self, other):
		if self.to_seconds() > other.to_seconds():
			return time1
		else:
			return time2

	def to_seconds(self):
		return self.hour * 60 * 60 + self.minute * 60 + self.second

	def show_time(self):
		print('{:02d}:{:02d}:{02d}'.format(
			self.hour, self.minute, self.second))