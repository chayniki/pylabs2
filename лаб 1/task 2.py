from task_1 import Table, Hero, Phone

if __name__ == "__main__":

    pers_1 = Hero(100, 20, 15)
    phone_1 = Phone("Samsung", "Galaxy S22", 30)
    table_1 = Table(3, 2, "wood")
    try:
        pers_1.heal_poison("+20")
    except TypeError:
        print("Ошибка: неправильные данные")

    try:
        phone_1.use(4)
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        table_1.resize(-1, 2)
    except ValueError:
        print("Ошибка: неправильные данные")