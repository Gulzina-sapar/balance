'''№ 1 '''

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(amount):
        print(f'Ваш счет пополнен на:{amount.balance}')

    def withdraw(amount):
        print(f'У вас недостаточно средств:{amount.balance}')

    def get_balance(amount):
        return f'{amount.balance}'

account = BankAccount('Gulzina',1500)
account.deposit()
account.withdraw()
print(f'Ваш баланс состовляет:{account.get_balance()}')
account.get_balance()
#
# ''' №2'''
#
# class Book:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
#
# class Library(Book):
#     def __init__(self,title,author,year):
#         self.books = []
#
#     def add_book(self,book):
#         self.books.append(book)
#
#     def remove_book(self,title):
#         pass
#
#     def find_book(self):
#         print(f'{Library.find_book()}')
#
#
# book1 = Book("1984","George Orwell",1949)
# book2 = Book(" To Kill a Mockingbird","Harper Lee", 1960)
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# print(library.find_book("1984"))

'''
1.Абстракция - это абстрагирование объекта кот. мы хотим описать.
'''


'''
2.Наследование - принцип кот наследуется от базового класса т.е от родительского.
'''
# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#      def white_cat(Cat):


'''
3.Полиморфизм - это один и тот же метод используестя в под классах как разные функции.
'''
# class Animal:
#     def sound(self):


'''
4.Инкапсуляция- кот.защищает от случайных изменений.защита полей.
getter -возвращает
del - удаляет
settery -определяет
protector -защищает раб.внутри класса вне класса нежелател.обрашатся но лучше нельза
но по согл.программмистов.
'''
# class Account:
#     def __init__(self,login,code):
#         self.login = login # public field
#         self.__code = code # privite field
#
#     @property
#     def get_code(self):# геттер - возвращает приватное поле
#         return self.__code
#
#
#     @get_code.setter
#     def get_code(self,new_code):# сеттер - тут мы прописываем логику обращение к этому полю
#         if not isinstance(new_code,int): # проверяем соответсвие кода - целому числу
#          raise ValueError('Код должен быть целым числом')
#         self.__code = new_code # Сеттер присваивает свой аргумент как новое значение
#                                 # к защищенному полю(_code)

    # @get_code.deleter # Удаление
    # def get.code(self)
    #  set.self.__code

# my_account = Account('@gmail.com', 123) # Создаем объект класса
# my_account.get_code = 123 #  Присваеиваем новое значение ч-з setter
# print((my_account.get_code)) # Получаем это(защищенное) поле ч-з  getter

'''Формируйте класс Bank с полями name,balance нужно инкапсулировать,
 например  balance не должен иметь более 3-х цифр'''

# class Bank:
#      def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance
#
#      @property
#      def get_balance(self):
#          return self.__balance
#
#      @get_balance.setter
#      def get_balance(self,new_balance):
#          if len(str(abs(new_balance))) > 3:
#              raise ValueError ('Длина должна быть меньше 3-х')
#          if not isinstance(new_balance,(float,int)):
#              raise TypeError ('Баланс должен быть числом!')
#          self.__balance = new_balance
#
# balance = Bank('My name', 543)
# balance.get_balance =150
# print(balance.get_balance)
#
# try:
#     balance.get_balance = 'str'  # Ошибка! Это не число.
# except TypeError as e:
#     print(f"Ошибка: {e}")

'''Формируйте класс  OpenUrls с атрибутом url должны быть инкапсулировть
url должен иметь правильный маршрут.Напр: должен иметь "https://"  и " " .'''

import webbrowser

class OpenUrls:
    def __init__(self, url):
        self.__url = url

    # Геттер
    @property
    def get_url(self):
        return self.__url

    # Сеттер где логика
    @get_url.setter
    def get_url(self, new_url):
        if 'https://' in new_url and '.' in new_url:
            self.__url = new_url
            webbrowser.open(new_url)
        else:
            raise ValueError('Неправильный адрес')


my_url = OpenUrls('http://instagram.com')
my_url.get_url = 'https://instagram.com'













 
