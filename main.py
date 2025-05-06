# """ООП"""
# ''' Не верный вариант'''
#
# class Car_BMW:
#     brand = None
#     color = None
#     price = None
#
# brand_car = Car_BMW.brand = 'BMW'
# color_car = Car_BMW.color = 'Blue'
# price_car = Car_BMW.price = 10.000
# print(brand_car,color_car,price_car)
#
# class Car_Mers:
#     name =None
#     age= None
#     color =None
#     price =None
#
# brand_car = Car_Mers.brand = 'Mers'
# color_car = Car_Mers.color = 'Blac'
# price_car = Car_Mers.price = 15.000
#
# print(brand_car,color_car,price_car)
#
# '''№ 2 Не совс.верный вариант '''
#
# class Car:
#     brand = None
#     color = None
#     price = None
#
# #  Первый объект
#
# brand_car_BMW = Car_brand = 'BMW'
# color_car_BMW = Car_color = 'Blue'
# price_car_BMW = Car_price = 10.000
#
# # Второй объект
#
# brand_car_Mers = Car.brand = 'Mers'
# color_car_Mers = Car.color = 'Blac'
# price_car_Mers = Car.price = 15.000
#
# print(brand_car_BMW,color_car_BMW,price_car_BMW)
# print(brand_car_Mers,color_car_Mers,price_car_Mers)
#
# ''' Урощенный вариант'''
#
# class Car:
#     def __init__(self,brand,color,price):
#       self.brand = brand
#       self.color = color
#       self.price =price
#
# data_car_bmw = Car('BMW', 'Blue',  10.000)
# data_car_mers = Car( 'Mers', 'Black', 15.000)
#
# print(data_car_bmw.brand,data_car_bmw.price,data_car_bmw.color)
# print(data_car_mers.brand,data_car_mers.price,data_car_mers.color)

# '''  Более упрощен.вариант Полиморфизм'''
#
# class Car:
#     def __init__(self,brand,color,price):
#        self.brand = brand
#        self.color = color
#        self.price =price
#
#     def get_data(self):
#         print(f' Бренд:{self.brand},цвет:{self.color},Цена:{self.price}')
#
# # Первый объект
# data_car_bmw = Car('BMW', 'Blue', 100.000)
# data_car_bmw.get_data()
#
# # # Второй объект
# #
# data_car_mers = Car( 'mers', 'Black', 150.000)
# data_car_mers.get_data()

''' Задание'''
#
# class Phone:
#     def __init__(self, brand,color,price,memory,new):
#         self.brand = brand
#         self.color = color
#         self.price =price
#         self.memory = memory
#         self.new = new
#
#     def get_data(self):
#
#           self.memory= 'Новый' if self.memory == True else 'Использован'
#
#           return f'''
#                   Бренд:{self.brand},
#                   Цвет:{self.color},
#                   Цена:{self.price},
#                   Память:{self.memory}
#                   '''
# phone1 = Phone('Samsung','red',100.00,'False','Использован')
#
# print(phone1.get_data())
#
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f'{self.name} is now siting')
#
#     def roll_over(self):
#         print(f'{self.name} rolled over!')
#
# my_dog = Dog('willie',6)
# your_dog =Dog('Rex',3)
# my_dog.sit()
# my_dog.roll_over()
#
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# print(f"Your dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.roll_over()


'''   '''
#
# class Restaurant:
#     def __init__(self,restaurant_name,cuizine_type):
#         self.restaurant_name = restaurant_name
#         self.cuizine_type = cuizine_type
#
#     def describe_restaurant(self):
#         print(f"Ресторан: {self.restaurant_name}")
#         print(f"Тип кухни:{self.cuizine_type}")
#         print()
#
#     def open_restaurant (self):
#         print(f"Ресторан {self.restaurant_name} открыт.")
#
# restaurant =Restaurant("Аврора","Итальянская кухня")
# restaurant2 = Restaurant("Dilbar","uzbekskoya")
# restaurant3 =Restaurant("Daididau","kazak")
#
# #print(restaurant.restaurant_name)
# #print(restaurant.cuizine_type)
#
# restaurant.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
#
# class Animals:
#     def __init__(self, view, age, color, breed):
#         self.view = view
#         self.age = age
#         self.color = color
#         self.breed = breed
#
#     def get_all_info(self):
#         return f'''
#                 Вид: {self.view},
#                 Возраст: {self.age},
#                 Цвет: {self.color},
#                 Порода: {self.breed}
#                 '''
#
#
# class Animals_on_Land(Animals):
#     def __init__(self, habitat, view, age, color, breed):
#         super().__init__(view, age, color, breed)
#         self.habitat = habitat
#
#     def get_all_info(self):
#         parent_info = super().get_all_info()
#         return f'{parent_info}Место обитания: {self.habitat}'
#
#
# animal_on_land = Animals_on_Land('Африка', "Хищник", 2, 'Желтый', 'Кошка')
# print(animal_on_land.get_all_info())

''' Задание.1.Создай класс Cat  с атрибутами:
name( имя кота), age(возраст кота).
Добавь методы: moew(self) - выводит на экран сообщение:
"Мяу! Меня зовут {name.} '''

# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def meow(self):
#         print(f'Мяу! Меня зовут {self.name}')
#
# cat = Cat('Иван',3)
# cat.meow()

'''Создать базовый класс Animals (type,speed,location).Умеют передвигаться.
Создать класс Cat().Умеет бегать.Просит накормить.
Создать класс Shark(). Умеет плавать.Охотиться на всех вокруг.
Создать класс Turtle(). Умеет ползать. '''

class Animals:
    def __init__(self,type,speed,location):
        self.type = type
        self.speed = speed
        self.location = location

    def move(self,a,b):
        self. a = a
        self.b = b
        return f'{self.a} {self.b}'

    def eats(self,food):
        self.food = food
        return self.food

class Cat(Animals):
    def __init__(self,type,speed,location):
        super().__init__(type.type, speed, location)

    def move(self,a,b):
        super().move(a,b)
        return f'{self.location} -{self.a} {self.b}'

    def eats(self,food):
        super().eats(food)
        return 'Накорми меня вот этим:',self.food




















