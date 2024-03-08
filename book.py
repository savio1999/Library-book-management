# Global list to store books
# (add, update, delete, list, and search by various attributes like title,
# author, or ISBN)
class library_book_management():
    def __init__(self):
        self.books = []

    def add_book(self,title, author, isbn):
        self.books.append({"title": title, "author": author, "isbn": isbn})

    def list_books(self):
        if not len(self.books):
            print("empty books list")

        for index,book in enumerate(self.books):
            print(f"index - {index}",book)
    
    def update_books(self,title, author, isbn,row):
        self.books[int(row)] = {"title": title, "author": author, "isbn": isbn}

    def delete_books(self,row):
        del self.books[int(row)]

    def search_books(self,field,value):
        for book in self.books:
            if book[field] == value:
                print(book)

            


