class Car:
    def __init__(self, brand: str, model: str, year: int, color: str) -> None:
        """
        Инициализация автомобиля
         brand - Марка автомобиля
         model - Модель автомобиля
         year - Год выпуска автомобиля
         color - Цвет автомобиля
        """
        self.brand = brand  # Публичный атрибут, так как марка не требует инкапсуляции
        self.model = model  # Публичный атрибут
        self.year = year  # Публичный атрибут
        self.color = color  # Публичный атрибут

    def __str__(self) -> str:
        """
        Магический метод __str__, возвращает строку:
        "Марка модель, год выпуска, цвет".
        return: Строка с характеристиками автомобиля
        """
        return f"{self.brand} {self.model}, {self.year}, {self.color}"

    def __repr__(self) -> str:
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}')"
    """
        Возвращает строку, позволяющую создать аналогичный объект.
        :return: Строковое представление конструктора класса
    """
    def drive(self) -> str:
        """
        Метод движения автомобиля
        return: Строка, описывающая движение автомобиля
        """
        return f"{self.brand} {self.model} едет."

class PassengerCar(Car):
    """
     Класс для легковых автомобилей. Наследуется от Car.
     Перегружает метод drive для описания отличий в движении.
        seats - Количество мест
    """
    def __init__(self, brand: str, model: str, year: int, color: str, seats: int) -> None:
        """
        Инициализация легкового автомобиля
        brand - Марка автомобиля
        model - Модель автомобиля
        year - Год выпуска автомобиля
        color - Цвет автомобиля
        seats - Количество мест в автомобиле
        """
        super().__init__(brand, model, year, color)
        self.seats = seats # Публичный атрибут, так как количество мест не требует инкапсуляции

    def __str__(self) -> str:
        """
        Перегруженный метод __str__, добавляет количество мест.
        Перегрузка магического метода __str__, возвращает строку:
        "Марка модель, год выпуска, цвет, количество мест"
        return: Строка с характеристиками автомобиля
        """
        return f"{super().__str__()}, {self.seats} мест."

    def drive(self) -> str:
        """
        Перегруженный метод движения автомобиля.
        "легковой автомобиль двигается быстрее, чем грузовой"
        return: Строка, описывающая движение легкового автомобиля
        """
        return f"{self.brand} {self.model} едет быстро."

class Truck(Car):
    """
    Класс для грузовых автомобилей. Наследуется от Car.
    Добавляет новый атрибут _payload_capacity с ограниченным доступом
    Включает метод load для загрузки груза.
        payload_capacity - Грузоподъемность в тоннах
    """
    def __init__(self, brand: str, model: str, year: int, color: str, payload_capacity: float) -> None:
        """
        Инициализация грузового автомобиля
        brand - Марка автомобиля
        model - Модель автомобиля
        year - Год выпуска автомобиля
        color - Цвет автомобиля
        payload_capacity - Грузоподъемность в тоннах
        """
        super().__init__(brand, model, year, color)
        self._payload_capacity = payload_capacity   # Защищенный атрибут, так как изменение требует контроля

    def __str__(self) -> str:
        """
        Перегрузка __str__ для грузового автомобиля
        Перегрузка магического метода __str__, возвращает строку:
        "Марка модель, год выпуска, цвет, грузоподъемность"
        return: Строка с характеристиками грузового автомобиля
        """
        return f"{super().__str__()}, {self._payload_capacity} тонн."

    def load(self, weight: float) -> str:
        """
        Метод загрузки груза
        weight - Вес груза в тоннах
        return: Сообщение об успешной загрузке или превышении грузоподъемности
        """
        if weight <= self._payload_capacity:
            return f"Груз в {weight} тонн успешно загружен в {self.brand} {self.model}."
        else:
            return f"Превышен лимит грузоподъемности! Максимальная грузоподъемность: {self._payload_capacity} тонн."

if __name__ == "__main__":
    # Создание экземпляра легкового автомобиля
    car1 = PassengerCar("Toyota", "Mark II", 1990, "Чёрный", 5)
    # Создание экземпляра грузовика
    car2 = Truck("Volvo", "FH16", 2022, "Синий", 20.0)

    # Вывод информации о легковом автомобиле
    print(car1)  # Используется метод __str__
    print(car1.drive())  # Используется перегруженный метод drive()

    # Вывод информации о грузовом автомобиле
    print(car2)  # Используется метод __str__
    print(car2.load(15))  # Используется метод load()
