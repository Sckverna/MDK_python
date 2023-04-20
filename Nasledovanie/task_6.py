class Time:
    def from_string(self,st):
        self.hour = int(st[:2])
        self.min = int(st[3:5])
        self.sec = int(st[6:])
    def __str__(self):
        print(f"{self.hour} : {self.min} : {self.sec}")
st = "22:45:30"
obj = Time()
obj.from_string(st)
obj.__str__()
