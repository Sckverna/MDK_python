class Queue:
    def __init__(self):
        self.inside = []
    def add(self,symb):
        self.inside.append(symb)
    def take_out(self):
        del self.inside[0]
    def __add__(self, other):
        self.inside.append(other)
    def __iadd__(self, other):
        self.inside.append(other)
    def __sub__(self, other):
        del self.inside[0]
    def __isub__(self, other):
        del self.inside[0]
    def __str__(self):
        return f"{'=>'.join(self.inside)}"
obj = Queue()
obj.add('lol')
obj + 'lel'
obj + 'kik'
print(obj)
obj-1
print(obj)

