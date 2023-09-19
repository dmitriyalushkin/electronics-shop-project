from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    def __str__(self):
        return f'{self.name}'


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity


    def get_number_of_sim(self, number_of_sim):
        self.number_of_sim = number_of_sim
        if number_of_sim <= 0:
            print(f'ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
        return self.number_of_sim


