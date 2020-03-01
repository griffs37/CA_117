#!usr/bin/env python

class Employee(object):

    next_employee_number = 0

    def __init__(self, name, hourly_rate=9.25, hours_worked=0.0):
        self.name = name
        self.rate = hourly_rate
        self.hours = hours_worked
        self.number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def add_hours(self, other):
        self.hours += other

    def __str__(self):
        return "Name: {}\nID: {}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}".format(self.name, self.number, self.hours, self.rate, (self.hours * self.rate))
