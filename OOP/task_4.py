class Car:
    def __init__(self,color,mark,cuse,speed,kpp):
        self.color = color
        self.mark = mark
        self.cuse = cuse
        self.speed = speed
        self.kpp = kpp
    def start(self):
        print("движение начато")
    def stop(self):
        print("движение прекращено")
    def turn(self):
        print("Машина повернула налево")
    def speed_up(self):
        self.speed += 10
        print("машина ускорена")
        if self.cuse == "truck":
            if self.speed >= 60:
                print("Скорость превышена! Разрешенная скорость 60 км/ч")
        else:
            if self.speed >= 60:
                print("Скорость превышена! Разрешенная скорость 60 км/ч")
    def speed_down(self):
        self.speed -= 10
        print("машина замедлена")
    def beep(self):
        print("beeeeeeeeeep")
truck = Car("red","lada","truck",20,"avto")
truck.start()
truck.turn()
truck.speed_up()
print(truck.speed)
truck.speed_down()
truck.beep()
truck.stop()
print("\n\n")
car = Car("green","toyota","sedan",50,"mex")
car.start()
car.turn()
car.speed_up()
print(car.speed)
car.speed_down()
car.beep()
car.stop()