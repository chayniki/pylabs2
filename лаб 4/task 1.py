class Vehicle:
    """
    Базовый класс для транспортных средств.
        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
    """

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """Возвращает репрезентацию транспортного средства для отладки."""
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"

    def start_engine(self) -> str:
        """Имитация запуска двигателя."""
        return f"Двигатель {self.brand} {self.model} запущен."


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(
        self, brand: str, model: str, year: int, doors: int, is_electric: bool
    ):
        """
        Описание экземпляра легкового автомобиля
        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        :param doors: Количество дверей в автомобиле.
        :param is_electric: Является ли автомобиль электрическим.
        """
        super().__init__(brand, model, year)
        self.doors = doors
        self.is_electric = is_electric

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        type_car = "Электрический" if self.is_electric else "Бензиновый"
        return f"{super().__str__()} ({type_car}, {self.doors} дверей)"

    def start_engine(self) -> str:
        """
        Перегрузка метода start_engine.
        Для электрических автомобилей возвращает соответствующее сообщение.
        """
        if self.is_electric:
            return f"{self.brand} {self.model}: Автомобиль включен (электродвигатель)."
        # Пример использования:


if __name__ == "__main__":
    vehicle = Vehicle("Generic", "Model-X", 2020)
    print(vehicle)
    print(repr(vehicle))
    print(vehicle.start_engine())

    car = Car("Tesla", "Model S", 2022, 4, True)
    print(car)
    print(repr(car))
    print(car.start_engine())