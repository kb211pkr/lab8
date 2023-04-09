import random


def main():
    separator = '\n' + '-' * 30 + '\n'
    globals_ = globals()

    for i in range(9, 10):
        print(separator)
        globals_.get(f'task{i}')()


def task1():
    class Bank:
        def __init__(self, __balance=0):
            self.__balance = float(__balance)

        def put(self, operation):
            if operation > 0:
                self.__balance += operation
            else:
                return False

        def withdraw(self, operation):
            if self.__balance >= operation > 0:
                self.__balance -= operation
            else:
                return False

        def check(self):
            print(f"Баланс на рахунку => {self.__balance}")

    test = Bank(0)
    test.check()
    test.put(10)
    test.check()
    test.withdraw(5)
    test.check()
    print(test.withdraw(10))


def task2():
    class Coin:
        def __init__(self, __sideup='heads'):
            if __sideup != 'heads' or __sideup != 'tails':
                self.__sideup = 'heads'
            self.__sideup = str(__sideup)

        def toss(self):
            if bool(random.getrandbits(1)):
                self.__sideup = 'heads'
                return 'heads'
            else:
                self.__sideup = 'tails'
                return 'tails'

    test = Coin()
    count = 0
    n = int(input('Кількість підкидань -> '))
    for i in range(n):
        if test.toss() == 'heads':
            count += 1

    print(f"З {n} підкидань => {count} 'heads'")
    print(f"З {n} підкидань => {n - count} 'tails'")


def task3():
    class Car:
        def __init__(self, brand='', model='', year=0):
            self.speed = 0
            self.brand = brand
            self.model = model
            self.year = year

        def accelerate(self):
            self.speed += 5

        def brake(self):
            if self.speed != 0:
                self.speed -= 5
            else:
                return False

        def get_speed(self):
            print(f"Швидкість => {self.speed}")

    test = Car()
    for i in range(5):
        test.accelerate()
        test.get_speed()
    for i in range(5):
        test.brake()
        test.get_speed()


def task4():
    class Pets:
        dogs = []

        def __init__(self, dogs):
            self.dogs = dogs

        def info(self):
            for dog in self.dogs:
                print(dog)

    class Dog:
        mammal = True
        nature = str
        breed = str

        def __init__(self, name, age): # атрибути екземпляру
            self.name = name
            self.age = age

        def __str__(self):
            return f"Dog's name is {self.name}, age is {self.age}, breed is {self.breed} and nature is {self.nature}"

        def voice(self):
            print('Gav')

        def jump(self):
            print('Jump')

    class Husky(Dog):
        nature = 'friendly'
        breed = 'Husky'

        def __init__(self, name, age):
            super().__init__(name, age)

        def voice(self):
            print('Gav-gav')

    class Pug(Dog):
        nature = 'lazy'
        breed = 'Pug'

        def __init__(self, name, age):
            super().__init__(name, age)

        def voice(self):
            print('Gav-gav-gav')

    class Bulldog(Dog):
        nature = 'aggressive'
        breed = 'Bulldog'

        def __init__(self, name, age):
            super().__init__(name, age)

        def voice(self):
            print('Gav-gav-gav-gav')

    dog1 = Husky('Bob', 5)
    dog2 = Pug('Jack', 3)
    dog3 = Bulldog('Tom', 7)
    dogs = Pets([dog1, dog2, dog3])
    dogs.info()
    dog1.voice()


def task5():
    class Buffer:
        def __init__(self):
            self.part = []

        def add(self, *a):
            a = [val for val in a if isinstance(val, int)]
            self.part.extend(a)
            while len(self.part) >= 5:
                print(f"{self.part[:5]} -> {sum(self.part[:5])}")
                self.part = self.part[5:]

        def get_current_part(self):
            return self.part

    test = Buffer()
    test.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    test.add('hello', 1, 2, 3)
    print(f"Saved -> {test.get_current_part()}")
    test.add(1, 2)


def task6():
    class StringError:
        @staticmethod
        def checkName(name):
            if len(name) >= 10:
                raise StringError('Name is too long')

    StringError.checkName('12345')
    StringError.checkName('12345678910')


def task7():
    class Convert:
        @staticmethod
        def toRoman(number):
            value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
            symbol = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
            i = 12
            str = ''

            while number:
                count = number // value[i]
                number %= value[i]
                while count:
                    str += symbol[i]
                    count -= 1
                i -= 1
            return str

        @staticmethod
        def toInt(number):
            symbol = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
                      'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
            i = 0
            num = 0

            while len(number) > i:
                if len(number) > i + 1 and number[i:i + 2] in symbol:
                    num += symbol[number[i:i + 2]]
                    i += 2
                else:
                    num += symbol[number[i]]
                    i += 1
            return num

    print(f"=> {Convert.toRoman(int(input('Введіть арабське число -> ')))}")
    print(f"=> {Convert.toInt(str(input('Введіть римське число -> ')))}")


def task8():
    from ClassList_task8 import Shop, Discount
    print("a)")
    store = Shop('Ювелірні вироби', 'ювелірка')
    print(f"Назва => {store.shop_name}")
    print(f"Тип => {store.store_type}")
    store.open_shop()
    store.describe_shop()

    print("b)")
    store1 = Shop('FS', 'свіжі фрукти')
    store2 = Shop('Tit', 'годинники')
    store3 = Shop('APRICITY', 'стильне взуття')
    store1.describe_shop()
    store2.describe_shop()
    store3.describe_shop()

    print("c)")
    store = Shop('Minimal', 'ювелірні вироби', 5)
    print(f"Кількість видів => {store.number_of_units}")
    store.number_of_units = 10
    print(f"Кількість видів => {store.number_of_units}")

    print("d)")
    print(f"Кількість видів => {store.set_number_of_units(15)}")
    print(f"Кількість видів => {store.increment_number_of_units(5)}")

    print("e)")
    store_discount = Discount(store.shop_name, ['ювелірні вироби'])
    store_discount.get_discounts_ptoducts()

    print("f)")
    all_store = [store, store1, store2, store3]
    all_store[0].describe_shop()


def task9():
    from User_task9 import User
    from Admin_task9 import Admin, Privileges
    print("a)")
    user_1 = User('Karyna', 'Polishchuk', 'krnplschk14@gmail.com', 'krn67', False)
    user_1.describe_user()
    user_1.greeting_user()
    user_2 = User('Карина', 'Поліщук', 'kb211_pkr@student.ztu.edu.ua', 'Karyna Polishchuk', True)
    user_2.describe_user()
    user_2.greeting_user()
    print("b)")
    print(f"Кількість користувачів {User.login_attempts}")
    print(f"Скидання {User.reset_login_attempts()}")
    print("c), d)")
    priv = Privileges(['can add post', 'can delete post', 'can ban user'])
    admin = Admin('Karyna', 'Polishchuk', 'krnplschk14@gmail.com', 'krn67', True, priv.privileges)
    priv.show_privileges()
    print("e)")
    admin.show_privileges()


if __name__ == "__main__":
    main()
