"""
Написать класс который, имеет поле array
и реализует инкапсуляцию по отношению array,
так чтобы она не оставалось пустым
и не присваивалось туда дублирующиеся значения

Написать набор классов,
которые реализуют методы:
 - get() - получает последний элемент из массива - array
 - update() - обновляет последний элемент из массива - array
 - pop() - удаляет последний элемент из массива - array
"""
# class WorkWithArray:
#     def __init__(self, array):
#         if not array:
#             raise ValueError("Массив не может быть пустым.")
#         if len(array) != len(set(array)):
#             raise ValueError("Массив содержит дублирующиеся значения.")
#         self._array = array
#
#     def get_all_array(self):
#         return self._array
#
#     @property
#     def array(self):
#         return self._array
#
#     @array.setter
#     def array(self, value):
#         if not value:
#             raise ValueError("Массив не может быть пустым.")
#         if len(value) != len(set(value)):
#             raise ValueError("Массив содержит дублирующиеся значения.")
#         self._array = value
#
#
# class GetArray(WorkWithArray):
#     def get(self):
#         if not self._array:
#             raise ValueError("Массив пуст.")
#         return self._array[-1]
#
#
# class UpdateArray(WorkWithArray):
#     def update(self, value):
#         if not self._array:
#             raise ValueError("Массив пуст.")
#         self._array[-1] = value
#
#
# class PopArray(WorkWithArray):
#     def pop(self):
#         if not self._array:
#             raise ValueError("Массив пуст.")
#         return self._array.pop()
#
#
# get_arr = GetArray([1, 2, 3])
# print(get_arr.get_all_array())
# print(get_arr.get())
#
# update_arr = UpdateArray([1, 2, 3])
# update_arr.update(5)
# print(update_arr.array)
#
# pop_arr = PopArray([1, 2, 5])
# print(pop_arr.pop())
# print(pop_arr.array)

#
# class WorkWithArray:
#     def __init__(self, array):
#         if not array:
#             raise ValueError("Массив не может быть пустым.")
#         if len(array) != len(set(array)):
#             raise ValueError("Массив содержит дублирующиеся значения.")
#         self._array = array
#
#     @property
#     def array(self):
#         return self._array
#
#     @array.setter
#     def array(self, value):
#         if not value:
#             raise ValueError("Массив не может быть пустым.")
#         if len(value) != len(set(value)):
#             raise ValueError("Массив содержит дублирующиеся значения.")
#         self._array = value
#
#
# class GetArray(WorkWithArray):
#     def __init__(self, array):
#         super().__init__(array)
#
#     def get(self):
#         return self._array[-1]
#
#
# class UpdateArray(WorkWithArray):
#     def __init__(self, array):
#         super().__init__(array)
#
#     def update(self, new_value):
#         if new_value in self._array:
#             raise ValueError("Нельзя добавлять дублирующее значение.")
#         self._array[-1] = new_value
#
#
# class PopArray(WorkWithArray):
#     def __init__(self, array):
#         super().__init__(array)
#
#     def pop(self):
#         return self._array.pop()
#
#
# # Пример использования:
# get_arr = GetArray([1, 2, 3])
# print("Get:", get_arr.get())
#
# upd_arr = UpdateArray([1, 2, 3])
# upd_arr.update(4)
# print("Update:", upd_arr.array)
#
# pop_arr = PopArray([1, 2, 3])
# print("Pop:", pop_arr.pop())
# print("After Pop:", pop_arr.array)
#
#
#
# def func(f):
#     def wrap():
#         print('a')
#         f()
#         print("y")
#
#     return wrap
#
# @func
# def say():
#     print('dec')
#
# say()
#
# try:
#     a = 4/2
#     print(a)
# except ZeroDivisionError:
#     print('на ноль делить не нельзя')
# except NameError:
#     print('на букву делить нельзя')


''' Варинат Асадбека'''

class WorkWithArray:
    def __init__(self, array):
        if not array:
            raise ValueError("Массив не может быть пустым.")
        if len(array) != len(set(array)):
            raise ValueError("Массив содержит дублирующиеся значения.")
        self._array = array

    def get_all_array(self):
        return self._array

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value):
        if not value:
            raise ValueError("Массив не может быть пустым.")
        if len(value) != len(set(value)):
            raise ValueError("Массив содержит дублирующиеся значения.")
        self._array = value


class GetArray(WorkWithArray):
    def get(self):
        if not self._array:
            raise ValueError("Массив пуст.")
        return self._array[-1]


class UpdateArray(WorkWithArray):
    def update(self, value):
        if not self._array:
            raise ValueError("Массив пуст.")
        self._array[-1] = value


class PopArray(WorkWithArray):
    def pop(self):
        if not self._array:
            raise ValueError("Массив пуст.")
        return self._array.pop()


get_arr = GetArray([1, 2, 3])
print(get_arr.get_all_array())
print(get_arr.get())

update_arr = UpdateArray([1, 2, 3])
update_arr.update(5)
print(update_arr.array)

pop_arr = PopArray([1, 2, 5])
print(pop_arr.pop())
print(pop_arr.array)


