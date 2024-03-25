from book import library_book_management
from storage import save_data,retrive_data
import os 


def main_menu():
    print("\nLibrary Management System")
    print("1. Manage books")
    print("2. Manage users")    
    print("3. Check out and check-in books")    
    print("4. save data")
    print("5. retrive data")
    print("6. Exit")
    choice = input("Enter choice: ")
    print()
    return choice

def main():
    book_management = library_book_management()
    while True:
        choice = main_menu()

        if choice == '1':
            while True:
                print("1. add books")
                print("2. update books")    
                print("3. delete book")    
                print("4. list book")    
                print("5. search books")  
                print("6. Go to main menu")  
                choice_1 = input("Enter choice: ")
                print()
                if choice_1 =="6":
                    break

                if choice_1 == '1':
                    title = input("Enter title: ")
                    author = input("Enter author: ") 
                    isbn = input("Enter ISBN: ")
                    book_management.add_book(title, author, isbn)
                    print("Book added.") 
                
                elif choice_1 == '2':
                    book_management.list_books()
                    row_number = input("Enter index_number: ")
                    title = input("Enter title: ")
                    author = input("Enter author: ") 
                    isbn = input("Enter ISBN: ")
                    book_management.update_books(title, author, isbn,row_number)
                    print("Book update.")

                elif choice_1 == '3':
                    book_management.list_books()
                    row_number = input("Enter index_number: ")
                    
                    book_management.delete_books(row_number)
                    print("Book deleted.")

                elif choice_1 == '4':
                    book_management.list_books()

                elif choice_1 == '5':
                    while True:
                        print("Search by")
                        print("1. title")
                        print("2. author")
                        print("3. isbn")
                        print("4. back")

                        row_number = input("Enter choice: ")
                        if row_number == "4":
                            break
                        if row_number == "1":
                            field = "title"
                            value = input("Enter title name: ")
                            book_management.search_books(field,value)
                        
                        elif row_number == "2":
                            field = "author"
                            value = input("Enter author name: ")

                            book_management.search_books(field,value)
                        elif row_number == "3":
                            field = "isbn"
                            value = input("Enter isbn name: ")

                            book_management.search_books(field,value)
                        else:
                            print("Invalid choice, please try again.")
                else:
                    print("Invalid choice, please try again.")
        if choice == '2':
            while True:
                print("1. add users")
                print("2. update users")    
                print("3. delete user")    
                print("4. list users")  
                print("5. search users")  
                print("6. Go to main menu")  
                choice_1 = input("Enter choice: ")
                print()
                if choice_1 =="6":
                    break

                if choice_1 == '1':
                    name = input("Enter name: ")
                    user_id = input("Enter user_id: ") 
                    book_management.add_user(name, user_id)
                    print("user added.") 
                
                elif choice_1 == '2':
                    book_management.list_user()
                    row_number = input("Enter row_number: ")
                    name = input("Enter name: ")
                    user_id = input("Enter user_id: ") 
                    book_management.update_users( name, user_id,row_number)
                    print("user update.")

                elif choice_1 == '3':
                    book_management.list_user()
                    row_number = input("Enter index_number: ")
                    
                    book_management.delete_users(row_number)
                    print("user deleted.")

                elif choice_1 == '4':
                    book_management.list_user()

                elif choice_1 == '5':
                    print("Search by")
                    print("1. name")
                    print("2. user_id")
                    
                    row_number = input("Enter choice: ")
                    if row_number == "1":
                        field = "name"
                        value = input("Enter name: ")
                        book_management.search_users(field,value)
                    
                    elif row_number == "2":
                        field = "user_id"
                        value = input("Enter user_id : ")

                        book_management.search_users(field,value)
                    else:
                        print("Invalid choice, please try again.")

        if choice == '3':
            while True:
                print("1. checkin book")
                print("2. checkout book")    
                print("3. Track book list")  
                print("4. Go to main menu")  
                choice_1 = input("Enter choice: ")
                print()
                if choice_1 =="4":
                    break

                if choice_1 == '1':

                    user_id = input("Enter user_id: ")
                    isbn = input("Enter isbn: ") 
                    book_management.checkin_book(user_id, isbn)
                    print("book checkin done.") 
                
                elif choice_1 == '2':

                    user_id = input("Enter user_id: ")
                    isbn = input("Enter isbn: ") 
                    book_management.checkout_book(user_id, isbn)
                    print("book checkout done.") 
                
                elif choice == '3':
                    # user_id = input("Enter user_id: ")
                    # isbn = input("Enter isbn: ") 
                    book_management.Track_book()
                    print("Track book list.") 

                else:
                    print("Invalid choice, please try again.")


        
        elif choice == '4':
            save_all_data = { 
                            "users":book_management.books(),
                            "books":book_management.users(),
                            }

            save_data(os.path.join("data", "save_all_data.json"),save_all_data)
            print("Saved Library data.") 

        elif choice == '5':
            file_path = os.path.join("data", "save_all_data.json")
            if os.path.isfile(file_path):
                json_data = retrive_data(file_path)
                book_management.load_users(json_data["users"]) 
                book_management.load_books(json_data["books"])

                print("retrived  Library data.") 
            else:
                print("data not found.") 

        elif choice == '6':
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
