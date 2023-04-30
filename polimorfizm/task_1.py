class Batary:
    def __init__(self, max_charge=5):
        self.capacity = [')',')',')',')',')']
        self.max_charge = max_charge
    def charge(self):
        if self.max_charge < 5:
            self.max_charge += 1
            self.capacity.append(')')
    def discharge(self):
        if self.max_charge > 0:
            self.max_charge -= 1
            self.capacity.pop()
    def __str__(self):
        if self.max_charge == 5:
            return f"{''.join(self.capacity)} - максимально заряженная батарея"
        else:
            return f"{''.join(self.capacity)} - заряд батареи"
obj = Batary()
obj.charge()
print(obj.max_charge)
print(obj)
obj.discharge()
print(obj)
