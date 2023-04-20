class Cat:
    def __init__(self,name = "akril",color = "red",age = 8):
        self.name=name
        self.color = color
        self.age = age
    def meow(self):
        print('meeeeooooow')
    def myr(self):
        print('myyyyyyr')
    def kis(self):
        print("kiskis")
cat = Cat()
print(cat.name)
print(cat.color)
print(cat.age)
cat.meow()
cat.myr()
cat.kis()