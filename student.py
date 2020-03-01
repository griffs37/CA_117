#!/usr/bin/env python

class Student(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.marks = {}
		self.results = ""

	def add_mark(self, module, mark):
		self.marks[module] = mark


	def check_mark(self):
		for module in self.marks:
			if self.marks[module] < 40:
				return False
		return True

	def check_overall(self):
		overall = sum(self.marks.values()) // len(self.marks.values())
		return overall


	def __str__(self):
		names = "Name:{}\nID:{}".format(self.name, self.tid)
		results = ""
		passed = ""
		overall = ""
		passed += "Passed" + ":" + str(self.check_mark())
		overall += "Overall" + ":" + str(self.check_overall())
		for module in sorted(self.marks):
			results += (str(module) + ":" + str(self.marks[module])) + "\n"

		return names + "\n" + results + passed + "\n" + overall + "\n"

	def __eq__(self, other):
		return self.check_overall() == other.check_overall()

	def __lt__(self, other):
		return self.check_overall() < other.check_overall()

	def __gt__(self, other):
		return self.check_overall() > other.check_overall()

	def __le__(self, other):
		return self.check_overall() <= other.check_overall()






s1 = Student('Daisy', 18341278)
s1.add_mark('CA116', 50)
s1.add_mark('CA110', 30)
s1.add_mark('CA117', 50)
s2 = Student('Poppy', 18123341)
s2.add_mark('CA116', 40)
s2.add_mark('CA123', 50)
s2.add_mark('CA117', 60)
print(s1)
print(s2)
print(s1 == s2)
print(s1 < s2)
print(s1 > s2)
print(s2 <= s1)


