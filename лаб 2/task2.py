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

    def __init__(self, id_: int, name: str, pages: int):
        # Инициализируем объект книги с id, названием и количеством страниц
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """Возвращает строку, позволяющую инициализировать такой же экземпляр книги."""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
# TODO: написать класс Library
class Library:
    """Класс для представления библиотеки."""

    def __init__(self, books=None):
        # Инициализируем библиотеку с пустым списком книг, если список не передан
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """Возвращает следующий идентификатор для добавления новой книги."""
        # Собираем множество существующих идентификаторов книг
        existing_ids = {book.id for book in self.books}
        next_id = 1
        # Ищем минимальный доступный идентификатор
        while next_id in existing_ids:
            next_id += 1
        return next_id

    def get_index_by_book_id(self, book_id):
        """Возвращает индекс книги по ее id."""
         # Проходим по всем книгам и ищем книгу с заданным идентификатором
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        # Если книга с таким id не найдена, вызываем ошибку с нужным сообщением
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
     # Создаем пустую библиотеку для тестирования
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

     # Создаем список книг из базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    # Инициализируем библиотеку с книгами
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    # Проверяем получение индекса книги по ее id
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
