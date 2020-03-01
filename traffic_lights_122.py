#!usr/bin/env python

import sys

class TrafficLight():

    def __init__(self, d, r, g):
        self.d = d
        self.r = r
        self.g = g
        self.time_till_switch = r
        self.colour = "r"

    def updateLights(self):
        self.time_till_switch -= 1
        if self.time_till_switch == 0 and self.colour is "r":
            self.colour = "g"
            self.time_till_switch = self.g
        elif self.time_till_switch == 0 and self.colour is "g":
            self.colour = "r"
            self.time_till_switch = self.r

    def getColour(self):
        return self.colour

    def getDistance(self):
        return self.d

    def getWaitTime(self):
        return self.time_till_switch

def main():
    traffic_lights = []
    L = int(sys.stdin.readline())
    for line in sys.stdin:
        lights = []
        strings = line.strip().split()
        for num in strings:
            lights.append(int(num))
        traffic_lights.append(TrafficLight(lights[0], lights[1], lights[2]))

    minutes_cycling = 0
    wait_time = 0
    for distance in range(0, L):
        for tl in traffic_lights:
            if distance == tl.getDistance():
                if tl.getColour() == "g":
                    tl.updateLights()
                    continue
                else:
                    minutes_cycling += tl.getWaitTime()
                    wait_time = tl.getWaitTime()
                    tl.updateLights()
                    continue
            tl.updateLights()
        for tl in traffic_lights:
            if wait_time > 0:
                for num in range(0, wait_time):
                    tl.updateLights()
        wait_time = 0
        minutes_cycling += 1
    print(minutes_cycling)

if __name__ == '__main__':
    main()
