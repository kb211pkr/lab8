
from User_task9 import User


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Привілеї => {self.privileges}")


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, mailing_list, privileges):
        super().__init__(first_name, last_name, email, nickname, mailing_list)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Привілеї => {self.privileges}")