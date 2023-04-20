from abc import abstractmethod
class User:
    def __init__(self,login,password):
        self.login = login
        self.password = password
    @abstractmethod
    def view(self):
        print("Я - User. Могу просматривать содержимое")

class Moderator(User):
    def __init__(self,login,password,group_id):
        super().__init__(login,password)
        self.group_id = group_id
    def view(self):
        print("Я - Moderator. Могу просматривать содержимое")
    def redact(self):
        print("Я - Moderator. Могу редактировать содержимое")
us = User("lol",123456)
us.view()
mod = Moderator("kek",654321,7)
mod.view()
mod.redact()