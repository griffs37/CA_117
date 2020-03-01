#!usr/bin/env python

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def __str__(self):
        return "Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, sum(self.d.values()))

    def add_time(self, sport, time):
        self.d[sport] = time

    def get_time(self, sport):
        return d[sport]
