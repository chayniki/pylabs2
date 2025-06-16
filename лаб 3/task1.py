class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        # Инициализация name и author
        self._name = name
        self._author = author

    @property
    def name(self):
        # Свойство для чтения name
        return self._name

    @property
    def author(self):
        # Свойство для чтения author
        return self._author

    def __str__(self):
        # Строковое представление
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        # Оф строковое представление
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        # Вызываем конструктор базового класса
        super().__init__(name, author)
        # Инициализация pages
        self.pages = pages

    @property
    def pages(self):
        # Свойство для чтения pages
        return self._pages

    @pages.setter
    def pages(self, value):
        # Проверка на тип и значение для pages
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        # Строковое представление
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        # Оф строковое представление
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        # Вызываем конструктор базового класса
        super().__init__(name, author)
        # Инициализация duration
        self.duration = duration

    @property
    def duration(self):
        # Свойство для чтения duration
        return self._duration

    @duration.setter
    def duration(self, value):
        # Проверка на тип и значение для duration
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом с плавающей запятой")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        # Строковое представление
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration} часов"

    def __repr__(self):
        # Оф строковое представление
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
