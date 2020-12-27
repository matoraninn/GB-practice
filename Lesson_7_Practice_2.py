from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    @property
    def consumption(self):
        return f"Суммарный расход ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}"
    @abstractmethod
    def abstract(self):
        return "Проверка"
class Coat(Clothes):
    def consumption(self):
        return f"Ткани для пальто: {self.param / 6.5 + 0.5 :.2f}"
    def abstract(self):
        pass
class Suit(Clothes):
    def consumption(self):
        return f"Ткани для костюма: {2 * self.param + 0.3 :.2f}"
    def abstract(self):
        return "Проверка"


coat = Coat(15.5)
suit = Suit(23)
print(coat.consumption())
print(suit.consumption())
print(suit.abstract())