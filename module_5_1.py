
class House: #Создаём класс House
    def __init__(self, name, number_of_floors): #Метод инициализации с названием ЖК и количеством этажей
        self.name = name #Создаём атрибут название
        self.number_of_floors = number_of_floors #Создаём атрибут количество этажей


    def go_to(self, new_floor): #Создаём метод на какой этаж приезжает лифт
        if new_floor <= self.number_of_floors and new_floor > 1: # условие для работы цикла
            for i in range(1,new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует')







# Создание объектов класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызов метода go_to
h1.go_to(5)
h2.go_to(10)