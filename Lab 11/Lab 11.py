#Nathan Gregorian Bailey
#Section 0003
#Program 11
#Created on November 17th 2021 
#Due November 19th 2021
import time
seconds = 0
class Clock():
    def __init__(self,hours=0,minutes=0,seconds=0,clock_type=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type
        


    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

    def __str__(self):
        if self.clock_type == 0:
            print("{:02}:{:02}:{:02}".format(self.hours,self.minutes,self.seconds))
        if self.clock_type == 1:
            if self.hours <= 12:
                print("{:02}:{:02}:{:02} am".format(self.hours,self.minutes,self.seconds))
            if self.hours > 12:
                self.hours = self.hours - 12
                print("{:02}:{:02}:{:02} pm".format(self.hours,self.minutes,self.seconds))

    



clock = Clock(int(input('What is the current hour ==> ')),int(input('What is the current minute ==> ')),int(input('What is the current second ==> ')),int(input('0 for 24 hour clock, 1 for 12 hour clock with am/pm ==> ')))

while seconds < 60:
    clock.__str__()
    clock.tick()
    time.sleep(1)
    seconds +=1
