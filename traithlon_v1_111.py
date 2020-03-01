#!/usr/bin/env python
 
class Triathlete(object):
 
    def __init__(self, name, n):
        self.name = name
        self.tid = n
 
    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)
 
class Triathlon(object):
 
    def __init__(self):
        self.d = {}
 
    def add(self, athlete):
        self.d[athlete.tid] = athlete
 
    def remove(self, athlete):
        del self.d[athlete]
 
    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        else:
            return None
 
def main():
 
    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
 
    tn.add(t1)
    tn.add(t2)
 
    t = tn.lookup(21)
    assert(t.tid)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)
 
    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)
 
if __name__ == '__main__':
    main()
