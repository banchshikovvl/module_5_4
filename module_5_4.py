#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта,
# тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):  # ,*args, **kwargs
        cls.houses_history.append(args[0])
        print(cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        return self.__le__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def go_to(self, new_floor):
        list_ = []
        for i in range(1, self.number_of_floors + 1):
            list_.append(i)
        if new_floor in list_:
            for j in range(1, new_floor + 1):
                if j != new_floor:
                    print(j)
                else:
                    print(f'Приехали на {new_floor} этаж {self.name}')
                    print()
        else:
            print(f'В {self.name},такого этажа не существует')


dom1 = House('ЖК Эльбрус', 30)
dom2 = House('ЖК Уют', 10)
dom3 = House('ЖК Речной', 20)

# House.go_to(dom1, 16)
# House.go_to(dom2, 9)

print()
print(f'{dom1.name}, количество этажей: {dom1.number_of_floors}')
print(f'{dom2.name}, количество этажей: {dom2.number_of_floors}')
print(f'{dom3.name}, количество этажей: {dom3.number_of_floors}')

del dom1
del dom2
print(House.houses_history, '- список зданий')

# print()
# print('Магический метод __str__:')
# print(dom1)
# print(dom2)
# print()
# print(f'Магический метод __len__: {dom1.name} {len(dom1)}, {dom2.name} {len(dom2)}')
# print()
# print('Метод "eq":', dom1 == dom2)
# print()
# print('Метод "add":', dom1 + 10)
# print(dom1 == dom2)
# print()
# dom1 += 10
# print('Метод "iadd":', dom1)
# print()
# print('Метод "radd":', 10 + dom2)
# print()
# print('Метод "gt":', dom1 > dom2)
# print()
# print('Метод "ge":', dom1 >= dom2)
# print()
# print('Метод "lt":', dom1 < dom2)
# print()
# print('Метод "le":', dom1 <= dom2)
# print()
# print('Метод "ne":', dom1 != dom2)
