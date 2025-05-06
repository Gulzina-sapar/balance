class MyArray:
    def __init__(self, initial_array=None):
        # Инициализация массива, если он передан, то добавляем элементы через add
        self._array = []
        if initial_array:
            for item in initial_array:
                self.add(item)

    @property
    def get_array(self):
        return self._array

    @get_array.setter
    def get_array(self, value):
        # Убедимся, что массив не пустой и не содержит дубли
        if not value:
            raise ValueError("Массив не может быть пустым.")

        # Проверка на дубли
        if len(value) != len(set(value)):
            raise ValueError("Массив не может содержать дублирующиеся значения.")

        # Если все проверки пройдены, присваиваем массив
        self._array = value

    def add(self, value):
        # Добавление нового элемента в массив, проверка на дубли
        if value in self._array:
            raise ValueError(f"Значение {value} уже присутствует в массиве.")
        self._array.append(value)

    def get(self):
        # Получить последний элемент из массива
        if not self._array:
            raise ValueError("Массив пуст.")
        return self._array[-1]

    def update(self, value):
        # Обновить последний элемент массива
        if not self._array:
            raise ValueError("Массив пуст.")
        if value in self._array:
            raise ValueError(f"Значение {value} уже присутствует в массиве.")
        self._array[-1] = value

    def pop(self):
        # Удалить последний элемент из массива
        if not self._array:
            raise ValueError("Массив пуст.")
        return self._array.pop()


get_arr = MyArray([1, 2, 3])
result = get_arr.get()
print(result)