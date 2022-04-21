class time:
    def __init__(self,h,m,s):
        self.hr = h 
        self.min = m
        self.sec = s
    def sub (self):
        pass
    def mul (self):
        pass
    def sec2time (self):
       time = self.sec * 60 / 3600
       print(time)
    def time2sec (self):
        time = self.hr * 3600
        print(time)

nemooneh = time (4,2,60)
nemooneh.sub()
nemooneh.mul()
nemooneh.sec2time()
nemooneh.time2sec()
