from task_1 import Tree, Car, Book # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # Инстанцируем все описанные классы
    book = Book("Metro 2033", "Dmitry Glukhovsky", 328)
    car = Car("Toyota", "Mark II", 1990)
    tree = Tree("дуб", 5.0, 10)
    # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
        print(book.read(-5)) # TODO: вызвать метод с некорректными аргументами(b)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        print(car.drive(-10)) # TODO: вызвать метод с некорректными аргументами(a)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        tree.grow(1.2) # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')
