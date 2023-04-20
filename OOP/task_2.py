class Good:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.calc()
    def calc(self):
        self.cost = self.weight*self.price
    def __str__(self):
        return f"{self.name}: {self.cost}"
apple = Good('apple', price = 100, weight = 1.5)
pear = Good('pear', price=120, weight=0.8)
print(apple)
print(pear)