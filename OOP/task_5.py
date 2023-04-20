from time import sleep
class Trafficlight:
    def __init__(self,color = "красный" ):
        self.color = color
    def switch(self):
        self.color = "красный"
        print(f"{self.color} свет")
        sleep(1)
        self.color = "желтый"
        print(f"{self.color} свет")
        sleep(0.5)
        self.color = "зеленый"
        print(f"{self.color} свет")
        sleep(2)
obj = Trafficlight()
obj.switch()
obj.switch()