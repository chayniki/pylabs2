import doctest
from typing import Union


class Hero:
    def __init__(
        self,
        health: Union[int, float],
        attack: Union[int, float],
        defence: Union[int, float],
    ):
        """
        Создание объекта "Герой"
        :param health: Здоровье персонажа (Должно быть не ниже нуля)
        :param attack: Атака персонажа (Должна быть положительным числом)
        :param defence: Защита персонажа (Должна быть положительным числом)
                                         (Подразумевается, что защита не превышает атаки персонажа)
        Примеры:
        >>> pers_1 = Hero(100, 20, 15) # инициализация экземпляра класса
        """

        if not isinstance(health, (int, float)):
            raise TypeError("Здоровье должно быть типа int или float")
        if health < 0:
            raise ValueError("Здоровье должно быть не ниже нуля")

        self.health = health

        if not isinstance(attack, (int, float)):
            raise TypeError("Атака должна быть типа int или float")
        if attack <= 0:
            raise ValueError("Атака должна быть положительным числом")

        self.attack = attack

        if not isinstance(defence, (int, float)):
            raise TypeError("Защита должна быть типа int или float")
        if defence <= 0:
            raise ValueError("Защита должна быть положительным числом")
        if defence > attack:
            raise ValueError("Защита не должна превышать атаку")

        self.defence = defence

    def heal_poison(self, heal_points: (int, float)) -> None:
        """
        Функция для восстановления здоровья персонажа
        :param heal_points: Восстановление заданного количества здоровья
        :raise ValueError: Ошибка об некорректном значении очков восстановления
        Пример:
        >>> pers_1 = Hero(70.1, 10.2, 8.3)
        >>> pers_1.heal_poison(20.9)
        """

        if not isinstance(heal_points, (int, float)):
            raise TypeError("Восстанавливаемое здоровье должно быть типа int или float")
        if heal_points < 0:
            raise ValueError(
                "Восстанавливаемое здоровье должно быть положительным числом"
            )

        self.health += heal_points

    def upgrade_attack(self, up_attack: (int, float) = 10) -> None:
        """
        Функция для улучшения атаки
        :param up_attack: Улучшает характеристики боя персонажа (по умолчанию повышение на 10 очков)
        Пример:
        >>> pers_1 = Hero(60, 20, 14)
        >>> pers_1.upgrade_attack()
        """

        if not isinstance(up_attack, (int, float)):
            raise TypeError("Улучшение должно быть типа int или float")
        if up_attack < 0:
            raise ValueError("Улучшение должно быть положительным числом")

        self.attack += up_attack

    def is_alive(self) -> bool:
        """
        Функция проверяющая жив ли персонаж
        :return: Живой ли персонаж
        Пример:
        >>> pers_1 = Hero(12, 30, 15)
        >>> pers_1.is_alive()
        True
        """

        if self.health == 0:
            return False
        else:
            return True


# ВТОРОЙ КЛАСС


class Table:
    def __init__(
        self, length: Union[int, float], width: Union[int, float], material: str
    ):
        """
        Создает объект стола.
        :param length: Длина стола в метрах, должна быть > 0.
        :param width: Ширина стола в метрах, должна быть > 0.
        :param material: Материал стола (например, дерево, металл).
        """
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть положительными числами.")
        self.length = length
        self.width = width
        self.material = material

    def calculate_area(self) -> (int, float):
        """
        Вычисляет площадь стола.
        :return: Площадь стола в квадратных метрах.
        >>> table = Table(2, 1, "wood")
        >>> table.calculate_area()
        2
        """
        return self.length * self.width

    def resize(
        self, new_length: Union[int, float], new_width: Union[int, float]
    ) -> None:
        """
        Изменяет размеры стола.
        :param new_length: Новая длина, должна быть > 0.
        :param new_width: Новая ширина, должна быть > 0.
        :raises ValueError: Если новые размеры не положительные.
        >>> table = Table(2, 1, "wood")
        >>> table.resize(3, 1.5)
        >>> table.length
        3
        """
        if new_length <= 0 or new_width <= 0:
            raise ValueError("Новые размеры должны быть положительными.")
        self.length = new_length
        self.width = new_width

    def describe(self, show_material: bool = True) -> str:
        """
        Возвращает описание стола.
        :param show_material: Указать, включать ли информацию о материале.
        :return: Строка с описанием стола.
        >>> table = Table(2, 1, "wood")
        >>> table.describe()
        'Стол размером 2x1 метра, сделан из wood.'
        """
        description = f"Стол размером {self.length}x{self.width} метра"
        if show_material:
            description += f", сделан из {self.material}."
        return description


# ТРЕТИЙ КЛАСС


class Phone:
    def __init__(self, brand: str, model: str, battery_level: int):
        """
        Создает объект телефона.
        :param brand: Бренд телефона (например, "Samsung").
        :param model: Модель телефона (например, "Galaxy S22").
        :param battery_level: Уровень заряда батареи в процентах (0–100).
        :raises ValueError: Если уровень заряда не находится в диапазоне 0–100.
        """
        if not (0 <= battery_level <= 100):
            raise ValueError("Уровень заряда должен быть от 0 до 100.")
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def charge(self, amount: int) -> None:
        """
        Заряжает телефон.
        :param amount: Количество процентов зарядки, должно быть > 0.
        :raises ValueError: Если зарядка превышает 100%.
        >>> phone = Phone("Apple", "iPhone 14", 50)
        >>> phone.charge(30)
        >>> phone.battery_level
        80
        """
        if amount <= 0:
            raise ValueError("Количество процентов зарядки должно быть положительным.")
        self.battery_level = min(100, self.battery_level + amount)

    def use(self, hours: int) -> None:
        """
        Использует телефон, разряжая батарею.
        :param hours: Время использования в часах, должно быть > 0.
        :raises ValueError: Если заряда недостаточно.
        >>> phone = Phone("Apple", "iPhone 14", 50)
        >>> phone.use(3)
        >>> phone.battery_level
        20
        """
        if hours <= 0:
            raise ValueError("Время использования должно быть положительным.")
        required_battery = hours * 10  # Допустим, телефон расходует 10% в час
        if required_battery > self.battery_level:
            raise ValueError("Недостаточно заряда для использования.")
        self.battery_level -= required_battery

    def get_status(self, include_battery: bool = True) -> str:
        """
        Возвращает описание телефона.
        :param include_battery: Указывать ли уровень заряда батареи.
        :return: Строка с описанием телефона.
        >>> phone = Phone("Samsung", "Galaxy S22", 75)
        >>> phone.get_status()
        'Телефон Samsung Galaxy S22, заряд батареи: 75%'
        """

        status = f"Телефон {self.brand} {self.model}"
        if include_battery:
            status += f", заряд батареи: {self.battery_level}%"
        return status


if __name__ == "__main__":
    doctest.testmod()