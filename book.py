from user import library_users_management

class library_book_management(library_users_management):
    """
    A class to represent a library book functionality.

    Methods
    -------
    add_book(title, author, isbn):
        Adds book to books database.

    list_books():
        Lists all books in the database

    update_books(title, author, isbn,row):
        Updates existing book in the database 
    
    delete_books(row):
        Deletes books in database 
    
    search_books(field,value):
        Lists books with searched details.

    load_books(books):
        retrives books data
    """

    def __init__(self):
        self.__books = []
        library_users_management.__init__(self)

    def add_book(self,title, author, isbn):
        self.__books.append({"title": title, "author": author, "isbn": isbn})

    def list_books(self):
        if not len(self.__books):
            print("empty books list")

        for index,book in enumerate(self.__books):
            print(f"index - {index}",book)
    
    def update_books(self,title, author, isbn,row):
        self.__books[int(row)] = {"title": title, "author": author, "isbn": isbn}

    def delete_books(self,row):
        del self.__books[int(row)]

    def search_books(self,field,value):
        
        for book in self.__books:
            if book[field] == value:
                print(book)
    
    def books(self):
        return self.__books

    def load_books(self,books):
        self.__books =books


