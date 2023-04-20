from abc import abstractmethod
class Stationary():
    def __init__(self,title):
        self.title = title
    @classmethod
    def set_color(cls,color):
        cls.color = color

    @abstractmethod
    def draw(self):
        pass
class Pen(Stationary):
    def __init__(self,color = "blue"):
        super().__init__("ручка")
        self.color = color
    def draw(self):
        print("ручка пишет")

class Pencil(Stationary):
    def __init__(self):
        super().__init__("карандаш")
    def draw(self):
        print("карандаш пишет")

class Handle(Stationary):
    def __init__(self):
        super().__init__("маркер")
    def draw(self):
        print("маркер пишет")

pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
stan = Stationary("канцелярия")
stan.set_color("yellow")
print(stan.color)
print(pen.color)
print(pencil.color)
print(handle.color)