#!/usr/bin/env python

class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.times = {}

	def __str__(self):
		return "Name: {}\nID: {}\nRace Time: {}".format(self.name, self.tid, sum(self.times.values()))

	def add_time(self, sport, time):
		self.times[sport] = time

	def get_time(self, sport):
		return self.times[sport]

	def __eq__(self, other):
		return sum(self.times.values()) == sum(other.times.values())

	def __lt__(self, other):
		return sum(self.times.values()) < sum(other.times.values())

	def __gt__(self, other):
		return sum(self.times.values()) > sum(other.times.values())

def main():

    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 150)
    t3.add_time('cycle', 120)
    t3.add_time('run', 100)

    print(t1)
    print(t2)
    print(t3)

    assert(t1 == t3)
    assert(t1 < t2)
    assert(t2 > t3)

if __name__ == '__main__':
    main()