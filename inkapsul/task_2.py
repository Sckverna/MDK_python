from abc import ABC, abstractmethod
class Cloth(ABC):
    def __init__(self,reserved):
        self._reserved = reserved
    @abstractmethod
    def podshet(self):
        pass
class Coat(Cloth):
    def podshet(self,V):

        self._reserved += V/6.5+0.5
    @property
    def reserved(self):
        return self._reserved
class Suit(Cloth):
    def podshet(self,H):
        self._reserved += 2*H+0.3
    @property
    def reserved(self):
        return self._reserved
c = Coat(0)
c.podshet(5)
print(c.reserved)
s = Suit(0)
s.podshet(5)
print(s.reserved)
print(s.reserved+c.reserved)



