
class User:
    login_attempts = 0

    def __init__(self, first_name, last_name, email, nickname, mailing_list):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.mailing_list = mailing_list
        self.increment_login_attempts()

    def describe_user(self):
        print(f"Повне ім'я => {self.last_name} {self.first_name}")

    def increment_login_attempts(self):
        User.login_attempts += 1
        return User.login_attempts

    @classmethod
    def reset_login_attempts(self):
        User.login_attempts = 0
        return User.login_attempts
    greeting_user = lambda self: print(f"Привіт, {self.nickname}!")
