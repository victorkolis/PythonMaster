class User:
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname

    def greeting(self):
        print('Hi, my name is:', self.name, self.nickname)


user = User('Victor', 'Kolis')
user.greeting()

# Deleting
# Deleting an attribute
del user.name

# Deleting
del user
