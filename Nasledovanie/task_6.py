class Time:
    def from_string(self,str):
        self.hour = int(str[:2])
        self.min = int(str[3:5])
        self.sec = int(str[6:])
str = "22:45:30"
obj = Time()
obj.from_string(str)
print(obj.hour)
print(obj.min)
print(obj.sec)