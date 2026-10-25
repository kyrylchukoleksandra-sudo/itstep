import datetime


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        return age


book1 = Book("Книга №1", "Автор №1", 2020)
print(book1.get_age())