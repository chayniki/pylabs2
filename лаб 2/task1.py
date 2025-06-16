BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
# TODO: написать класс Book
class Book:
    """Класс для представления книги."""
 # Инициализация атрибутов объекта Book
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_ # Уникальный id книги
        self.name = name # Название книги
        self.pages = pages # Количество страниц

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """Возвращает строку, позволяющую инициализировать такой же экземпляр книги."""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

if __name__ == '__main__':
    # Инициализируем список книг на основе данных из BOOKS_DATABASE
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
# Проверяем метод __str__ для каждого объекта в списке
    for book in list_books:
        print(book)  # проверяем метод __str__    # Должен вывести название

 # Проверяем метод __repr__, выводя весь список книг
    print(list_books)  # проверяем метод __repr__    # Должен вывести строки, с помощью которых можно создать такие же объекты
