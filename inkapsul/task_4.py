from task_3_Box import *
class Truck:
    def __init__(self,mark = 'maz',color = 'green', capacity = []):
        self.capacity = capacity
        self.mark = mark
        self.color = color
    def __add__(self, other):
        self.capacity.append(other.postcode)
    def __sub__(self, other):
        del self.capacity[0]
    def __str__(self):
        return f"поссылки: {'=>'.join([str(enum) for enum in self.capacity])}"
box1 = Box(randint(100000, 999999),"pavlik",'kazan','moscow')
box2 = Box(randint(100000, 999999),"oleg",'yfa','moscow')
box3 = Box(randint(100000, 999999),"adel",'NiNo','pekin')
print(box1.postcode)
print(box1.name)
print(box1.from_city)
print(box1.target_city)
box1.target_city = "pekin"
print(box1.target_city)
truck = Truck()
truck+box1
truck+box2
truck+box3
print(truck)
truck-1
print(truck)