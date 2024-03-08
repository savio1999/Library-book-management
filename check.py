

class check_book_management():
    def __init__(self):
        self.checkout_list = []
        self.checkin_list = []

    def checkout_book(self,user_id, isbn):
        checkout_list.append({"user_id": user_id, "isbn": isbn})

    def checkin_book(self,user_id, isbn):
        checkin_list.append({"user_id": user_id, "isbn": isbn})

    def Track_book(self):
        if not self.checkout_list:
            print("empty checkout list")
        for checkout in self.checkout_list:
            print(checkout)
        if not self.checkin_list:
            print("empty checkin list")
        
        for checkin in self.checkin_list:
            print(checkin)


        
