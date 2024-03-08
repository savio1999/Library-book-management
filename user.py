

class library_users_management():
    def __init__(self):
        self.users = []
        # self.users = [{'name': 'savio', 'user_id': '1'}]

    def add_user(self,name, user_id):
        self.users.append({"name": name, "user_id": user_id})

    def list_user(self):
        for index,user in enumerate(self.users):
            print(f"index - {index}",user)

    def update_users(self,name, user_id,row):
        self.users[int(row)] = {"name": name, "user_id": user_id}

    def delete_users(self,row):
        del self.users[int(row)]

    def search_users(self,field,value):
        for user in self.users:
            if user[field] == value:
                print(user)