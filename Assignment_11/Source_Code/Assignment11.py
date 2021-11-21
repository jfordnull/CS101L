########################################################################
##
## CS 101 Lab
## Program #11
## Jacob Ford
## jwfhmp@umkc.edu
##
########################################################################

import time

class Clock:
    def __init__(self, hour, min, sec, clocktype = 0):
        self.clocktype = clocktype
        self.hour = hour
        self.min = min
        self.sec = sec
    
    def __str__(self):
        if self.clocktype == 0:
            return '{:02}:{:02}:{:02}'.format(self.hour,self.min,self.sec)
        elif self.clocktype == 1:
            if self.hour == 0:
                return '12:{:02}:{:02} am'.format(self.min,self.sec)
            elif self.hour < 12:
                return '{:02}:{:02}:{:02} am'.format(self.hour,self.min,self.sec)
            elif self.hour == 12:
                return '12:{:02}:{:02} pm'.format(self.min,self.sec)
            elif self.hour > 12:
                return '{:02}:{:02}:{:02} pm'.format(self.hour - 12,self.min,self.sec)
    
    def tick(self):
        self.sec += 1
        if self.sec >= 60:
            self.min += 1
            self.sec -= 60
        if self.min >= 60:
            self.hour += 1
            self.min -= 60

def main():
    hour = int(input('What is the current hour ==> '))
    min = int(input('What is the current minute ==> '))
    sec = int(input('What is the current second ==> '))
    clock = Clock(hour,min,sec, 1)
    while True:
        print(clock)
        clock.tick()
        time.sleep(1)

main()