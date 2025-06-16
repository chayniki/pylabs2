import doctest
class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Инициализация дерева.
        :param species: Вид дерева ('дуб', 'сосна' и т.д).
        :param height: Высота дерева в метрах (больше 0).
        :param age: Возраст дерева в годах (больше 0).
        """
        if not isinstance(species, str):
            raise TypeError("species должен быть строкой.")
        if not isinstance(height, (int, float)):
            raise TypeError("height должен быть числом.")
        if not isinstance(age, int):
            raise TypeError("age должен быть целым числом.")

        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> str:
        """
        Фун-я увеличивает возраст и высоту дерева.
        :param years: Количество лет, на которое нужно увеличить возраст (больше 0).
        :return: Сообщение о росте дерева.
        >>> tree = Tree('дуб', 5, 10)
        >>> tree.grow(5)
        'Дерево выросло на 5 лет и теперь имеет высоту 6.0 метров.'
        """
        if not isinstance(years, int):
            raise TypeError("years должен быть целым числом.")
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")

        self.age += years
        self.height += years * 0.2  # Дерево растет на 0.4 м в год
        return f"Дерево выросло на {years} лет и теперь имеет высоту {self.height:.1f} метров."

    def get_info(self) -> str:
        """
        Возвращает информацию о дереве.
        :return: Строка с информацией о дереве.
        >>> tree = Tree('дуб', 5, 10)
        >>> tree.get_info()
        'Дерево: дуб, высота: 5.0 м, возраст: 10 лет.'
        """
        return f"Дерево: {self.species}, высота: {self.height:.1f} м, возраст: {self.age} лет."


class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация автомобиля.
        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска (не меньше 1910).
        :raises ValueError: Если год меньше 1910.
        """
        if year < 1910:
            raise ValueError("Год выпуска не может быть меньше 1910.")

        self.make = make
        self.model = model
        self.year = year

    def drive(self, distance: float) -> str:
        """
        Поездка на автомобиле на расстояние.
        :param distance: расстояние в километрах (больше 0).
        :raises ValueError: Если расстояние меньше 0.
        :return: Строка с сообщением о поездке.
        >>> car = Car("Toyota", "Mark II", 1990)
        >>> car.drive(15)
        'Вы проехали 15 километров на Toyota Mark II.'
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным.")

        return f'Вы проехали {distance} километров на {self.make} {self.model}.'

    def get_age(self, current_year: int) -> int:
        """
        Получение возраста автомобиля.
        :param current_year: Текущий год.
        :return: Возраст автомобиля.
        >>> car = Car("Toyota", "Mark II", 1990)
        >>> car.get_age(2023)
        33
        """
        return current_year - self.year


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц (больше 0).
        :raises ValueError: Если количество страниц меньше 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int) -> str:
        """
        Чтение определенного количества страниц.
        :param pages_to_read: Количество страниц для чтения (больше 0).
        :raises ValueError: Если количество страниц для чтения меньше 0.
        :return: Строка с сообщением о прочитанных страницах.
        >>> book = Book("Metro 2033", "Dmitry Glukhovsky", 328)
        >>> book.read(50)
        'Вы прочитали 50 страниц из 328.'
        """
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом.")

        return f'Вы прочитали {pages_to_read} страниц из {self.pages}.'

    def get_info(self) -> str:
        """
        Получение информации о книге.
        :return: Строка с информацией о книге.
        >>> book = Book("Metro 2033", "Dmitry Glukhovsky", 328)
        >>> book.get_info()
        'Книга "Metro 2033" написана Dmitry Glukhovsky и содержит 328 страниц.'
        """
        return f'Книга "{self.title}" написана {self.author} и содержит {self.pages} страниц.'

if __name__ == "__main__":
    doctest.testmod()
