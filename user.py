from check import check_book_management

class library_users_management(check_book_management):
    """
    A class to represent a library user functionality.

    Methods
    -------
    add_user(title, author, isbn):
        Adds user to users database.

    list_user():
        Lists all users in the database

    update_users(title, author, isbn,row):
        Updates existing users in the database 
    
    delete_users(row):
        Deletes users in database 
    
    search_users(field,value):
        Lists users with searched details.

    load_users(users):
        retrives users data       
    """

    def __init__(self):
        self.__users = []
        check_book_management.__init__(self)

    def add_user(self,name, user_id):
        self.__users.append({"name": name, "user_id": user_id})

    def list_user(self):
        if not len(self.__users):
            print("empty users list")

        for index,user in enumerate(self.__users):
            print(f"index - {index}",user)

    def update_users(self,name, user_id,row):
        self.__users[int(row)] = {"name": name, "user_id": user_id}

    def delete_users(self,row):
        del self.__users[int(row)]

    def search_users(self,field,value):
        for user in self.__users:
            if user[field] == value:
                print(user)
    
    def users(self):
        return self.__users

    def load_users(self,users):
        self.__users = users