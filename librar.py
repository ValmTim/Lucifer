from re import A

class Book:
    
    def __init__(self, book, author, data, publisher, description):
        self.book = book.strip()
        self.author = author.strip()
        self.data = data.strip()
        self.publisher = publisher.strip()
        self.description = description.strip()
    
    
    def print(self):
        
        print(f"Название книги : {self.book}\n"
              f"Автор книги: {self.author}\n"
              f"Год публикации : {self.data}\n"
              f"Издатель книги: {self.publisher}\n"
              f"Описание книги: {self.description}\n")

    ## Функция возвращающая название книги
    def get_book(self):
        return self.book

    ## Функция изменения названия книги
    def set_book(self, name):
        self.book = book

    ## Функция возвращения автора книги
    def get_author(self):
        return self.author

    ## Изменение автора книги
    def set_author(self, author):
        self.author = author

    ## Функция возвращающая дату публикации книги
    def get_data(self):
        return self.data

    ## Изменение даты публикации книги
    def set_data(self, data):
        self.data = data

    ## Функция, возвращающая издателя книги
    def get_publisher(self):
        return self.publisher

    ## Изменение издателя книги
    def set_publisher(self, publisher):
        self.publisher = publisher

    ## Функция, возвращающая описание книги
    def get_description(self):
        return self.description

    ## Изменение описания книги
    def set_description(self, description):
        self.description = description
        
def get_field(help_str, old_val):
        a = input(help_str).strip()
        if a != '':
            
            return a
        return old_val

def save(library):
  f = open('library.txt', 'w', encoding="utf-8")
  for i in library:
    f.write(str(i.book)+'.'+str(i.author)+'.'+str(i.data)+'.'+str(i.publisher)+'.'+str(i.description)+"\n")

##Функции библиотеки 
Library = []
fLibrary = open('library.txt', encoding="utf-8")  #library-библиотека(список книг)
for line in fLibrary:
  Library.append(Book(line.split(".")[0], line.split(".")[1], line.split(".")[2], line.split(".")[3], line.split(".")[4]))

while True:
    print(f"Введите числа от 1 до 6, чтобы:\n"
          f"1 - Список всех книг в библиотеке\n"
          f"2 - Добавить новую книгу\n"
          f"3-  Изменить существующую книгу\n"
          f"4 - Поиск книги\n"
          f"5 - Удалить книгу\n"
          f"6 - Выход из программы")
    n = input()
    if n == "1":
        print(f"СПИСОК КНИГ:")
        ## Вывод списка книг, существующих в библиотеке
        for i in range(len(Library)):
            print(f"КНИГА №{i+1}")
            Library[i].print()
    elif n == "2":
        print(f"Введите данные новой книги:")
        book = input("Название книги: ")
        author = input("Автор книги: ")
        data = input("Год публикации: ")
        publisher = input("Издатель книги: ")
        description = input("Описание книги: ")
        ## Добавление новой книги в список книг
        Library.append(Book(book, author, data, publisher, description))
        save(Library)
    elif n == "3":
        print(f"Введите данные изменённой книги:\n")
        book_num = int(input("Изменение книги №"))
        if book_num > len(Library):
          print("Неверная цифра")
          continue
        book = get_field("Название Книги("+Library[book_num-1].book+'): ', Library[book_num-1].get_book())
        author = get_field("Автор("+Library[book_num-1].author+'): ', Library[book_num-1].get_author())
        data = get_field("Год Публикации("+Library[book_num-1].data+'): ', Library[book_num-1].get_data())
        publisher = get_field("Издатель( )"+Library[book_num-1].publisher+'): ', Library[book_num-1].get_publisher())
        description = get_field("Описание( )"+Library[book_num-1].description+'): ', Library[book_num-1].get_description())
        Library[book_num-1] = Book(book, author, data, publisher, description)
        save(Library)
    elif n == "5":
        ## Удаляем книгу
        book_num = int(input("Удаление книги №"))
        if book_num > len(Library):
          print("Неверная цифра")
          continue

        del Library[book_num-1] 
        save(Library)
    elif n == "4":
        poisk = input("Введите название книги: ")
        result = filter(lambda book: poisk.lower() in book.book.lower(),Library)
        for i, book in enumerate(result, 1):
            print(f"КНИГА №{i}")
            book.print()
    elif n == "6":
        ## Завершение работы
        break
    else:
        print("ERROR!")
print("Выход!")