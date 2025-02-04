class Book:
    """
    Базовый класс для представления книги.
    """

    def __init__(self, name: str, author: str):
        """
        Инициализирует объект книги.
        """

        self._name = name  # Защищенное поле для названия книги
        self._author = author  # Защищенное поле для автора книги

    @property
    def name(self):
        """
        Возвращает название книги.
        """

        return self._name

    @property
    def author(self):
        """
        Возвращает автора книги.
        """

        return self._author

    def __str__(self):
        """
        Возвращает строковое представление объекта книги.
        """

        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладки.
        """

        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Класс для представления бумажной книги, наследуется от Book.
    """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализирует объект бумажной книги.
        """

        super().__init__(name, author)  # Вызов конструктора родительского класса
        self.pages = pages  # Инициализация количества страниц через сеттер

    @property
    def pages(self):
        """
        Возвращает количество страниц в книге.
        """

        return self._pages

    @pages.setter
    def pages(self, value):
        """
        Устанавливает количество страниц, проверяя корректность значения.
        """

        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError(
                "Количество страниц должно быть положительным целым числом."
            )
        self._pages = value

    def __str__(self):
        """
        Возвращает строковое представление объекта бумажной книги.
        """
        return (
            f"Книга {self.name} (бумажная). Автор {self.author}. Страниц: {self.pages}"
        )

    class AudioBook(Book):
        """
        Класс для представления аудиокниги, наследуется от Book.
        """

        def __init__(self, name: str, author: str, duration: float):
            """
            Инициализирует объект аудиокниги.
            """
            super().__init__(name, author)  # Вызов конструктора родительского класса
            self.duration = duration  # Инициализация продолжительности через сеттер

        @property
        def duration(self):
            """
            Возвращает продолжительность аудиокниги.
            """
            return self._duration

        # Сеттер проверяет тип данных и гарантирует, что продолжительность книги является положительным числом.
        @duration.setter
        def duration(self, value):
            """
            Устанавливает продолжительность аудиокниги, проверяя корректность значения.
            """
            if not isinstance(value, (int, float)):
                raise TypeError("Продолжительность должна быть числом.")
            if value <= 0:
                raise ValueError("Продолжительность должна быть положительным числом.")
            self._duration = value

        def __str__(self):
            """
            Возвращает строковое представление объекта аудиокниги.
            """
            return f"Книга {self.name} (аудио). Автор {self.author}. Длительность: {self.duration} часов"