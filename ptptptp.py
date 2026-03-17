import pickle
import os
from abc import ABC, abstractmethod

PICKLE_FILE = "library_data.pkl"  

class Person(ABC):
    def __init__(self, name):
        self._name = name
    
    @abstractmethod
    def menu(self):
        pass

class Book:
    def __init__(self, title, author, status="доступна"):
        self.title = title
        self.author = author
        self.status = status

class User:
    def __init__(self, name, books=None):
        self.name = name
        self.books = books or []

class Librarian(Person):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = library
    
    def menu(self):
        while True:
            print("nВы вошли как библиотекарь, доступные действия:")
            print("1 - добавить книгу")
            print("2 - удалить книгу")
            print("3 - зарегистрировать пользователя")
            print("4 - показать список пользователей")
            print("5 - показать список всех книг")
            print("0 - назад")
            choice = input("выберите: ")
            
            if choice == "1":
                self.library.add_book()
            elif choice == "2":
                self.library.remove_book()
            elif choice == "3":
                self.library.register_user()
            elif choice == "4":
                self.library.show_users()
            elif choice == "5":
                self.library.show_books()
            elif choice == "0":
                break
            else:
                print("кажется, ввод был неправильным!!")

class Reader(Person):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = library
    
    def menu(self):
        while True:
            print("\n1 - доступные книги")
            print("2 - взять книгу")
            print("3 - вернуть книгу")
            print("4 - мои книги")
            print("0 - назад")
            choice = input("выберите: ")
            
            if choice == "1":
                self.library.show_available_books()
            elif choice == "2":
                self.library.take_book(self._name)
            elif choice == "3":
                self.library.return_book(self._name)
            elif choice == "4":
                self.library.show_user_books(self._name)
            elif choice == "0":
                break
            else:
                print("кажется, ввод был неправильным!!")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()
    
    def load_data(self):
      
        if os.path.exists(PICKLE_FILE):
            try:
                with open(PICKLE_FILE, "rb") as f:
                    data = pickle.load(f)
                self.books = data.get("books", [])
                self.users = data.get("users", [])
                print("Данные успешно загружены из library_data.pkl!!!")
                return
            except Exception as e:
                print(f"Ошибка при загрузке pickle: {e}")
        else:
            print("Файл library_data.pkl не найден!!!")
    
    def save_data(self):

        try:
            with open(PICKLE_FILE, "wb") as f:
                pickle.dump({"books": self.books, "users": self.users}, f)
        except Exception as e:
            print(f"Не получилось чтото в  pickle: {e}")
    

    def add_book(self):
        title = input("Название книги: ")
        author = input("Автор: ")
        self.books.append(Book(title, author))
        self.save_data()
        print(f"Книга '{title}' добавлена!!")
    
    def remove_book(self):
        title = input("Название книги для удаления: ")
        book = next((b for b in self.books if b.title == title), None)
        if not book:
            print("Книга не найдена...")
            return
        for user in self.users:
            if title in user.books:
                print("Ой, нельзя удалить выданную книгу!!")
                return
        self.books.remove(book)
        self.save_data()
        print(f"Книга '{title}' удалена!!")
    
    def register_user(self):
        name = input("Имя нового пользователя: ")
        if any(u.name == name for u in self.users):
            print("Пользователь с таким именем уже существует :(")
            return
        self.users.append(User(name))
        self.save_data()
        print(f"Пользователь '{name}' зарегистрирован!!")
    
    def show_users(self):
        if not self.users:
            print("Список пользователей пуст...")
            return
        print("ВСЕ ПОЛЬЗОВАТЕЛИ:")
        for i, user in enumerate(self.users, 1):
            books = ", ".join(user.books) if user.books else "нет"
            print(f"{i}. {user.name} - книги: {books}")
    
    def show_books(self):
        if not self.books:
            print("Список книг пуст...")
            return
        print("ВСЕ КНИГИ:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. '{book.title}' ({book.author}) - [{book.status}]")

    def show_available_books(self):
        available = [b for b in self.books if b.status == "доступна"]
        if not available:
            print("нет доступных книг...")
            return
        print("ВСЕ ДОСТУПНЫЕ КНИГИ:")
        for i, book in enumerate(available, 1):
            print(f"{i}. '{book.title}' ({book.author})")
    
    def take_book(self, user_name):
        title = input("Какую книгу хотите взять? ")
        for book in self.books:
            if book.title == title:
                if book.status == "выдана":
                    print("Ой, книгу забрал другой пользователь...")
                    return
                book.status = "выдана"
                for u in self.users:
                    if u.name == user_name:
                        u.books.append(title)
                        break
                self.save_data()
                print(f"Книга '{title}' выдана вам!!")
                return
        print("книга, кажется, не найдена...")
    
    def return_book(self, user_name):
        if not any(user_name == u.name and u.books for u in self.users):
            print("а у вас нет книг для возврата...")
            return
        print("Ваши доступные книги:")
        for u in self.users:
            if u.name == user_name:
                for i, title in enumerate(u.books, 1):
                    print(f"{i}. {title}")
                break
        try:
            num = int(input("Номер книги для возврата: "))
            for u in self.users:
                if u.name == user_name and 1 <= num <= len(u.books):
                    book_title = u.books.pop(num - 1)
                    for book in self.books:
                        if book.title == book_title:
                            book.status = "доступна"
                            break
                    self.save_data()
                    print(f"Книга '{book_title}' возвращена")
                    return
            print("номер, кажется, неправильный...")
        except ValueError:
            print("кажется, ввод был неправильным!!")
    
    def show_user_books(self, user_name):
        for u in self.users:
            if u.name == user_name:
                if not u.books:
                    print("У вас пока нет книг!!")
                    return
                print("Ваши доступные книги:")
                for i, title in enumerate(u.books, 1):
                    print(f"{i}. {title}")
                return

def main():
    library = Library()
    print("Вы вошли в библиотеку:")
    print("1 - войти как библиотекарь")
    print("2 - войти как пользователь")
    print("0 - выйти из библиотеки")
    choice = input("выберите: ")
    
    name = input("Введите имя: ")
    
    if choice == "1":
        librarian = Librarian(name, library)
        librarian.menu()
    elif choice == "2":
        reader = Reader(name, library)
        reader.menu()
    elif choice == "0":
        print("Данные сохранены, пока!!")
    else:
        print("кажется, ввод был неправильным!!")


main()