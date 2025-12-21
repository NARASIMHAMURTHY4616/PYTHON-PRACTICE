from abc import ABC , abstractmethod
class a(ABC):
    @abstractmethod
    def mone(self):
        pass
class b(a):
    def mone(self):
        print("welcome")
class c(a):
    def mone(self):
        print("helo")
obj1=b()
obj2=c()
obj1.mone()
obj2.mone()
