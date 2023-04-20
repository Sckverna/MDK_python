class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Child(Father):
    def __init__(self, patronim):
        super().__init__("tom","lolik")
        self.patronim = patronim
obj = Child("antonovisch")
print(obj.name)
print(obj.surname)
print(obj.patronim)