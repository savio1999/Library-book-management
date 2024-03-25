

class check_book_management():

    """
    A class to represent a library books checkin and checkout functionality.

    Methods
    -------
    checkout_book(self,user_id, isbn):
        Adds checkout book to database.

    checkin_book(self,user_id, isbn):
        Adds checkin book to database.

    Track_book(self):
        Lists track of checkin and checkout of books.  

    """
    def __init__(self):
        self.__checkout_list = []
        self.__checkin_list = []

    def checkout_book(self,user_id, isbn):
        self.__checkout_list.append({"user_id": user_id, "isbn": isbn})

    def checkin_book(self,user_id, isbn):
        self.__checkin_list.append({"user_id": user_id, "isbn": isbn})

    def Track_book(self):
        if not self.__checkout_list:
            print("empty checkout list")

        else:
            print("Checkout List")
            for checkout in self.__checkout_list:
                print(checkout)

        if not self.__checkin_list:
            print("empty checkin list")

        else:
            print("checkin  list")
            for checkin in self.__checkin_list:
                print(checkin)


        
