class User:
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname


user = User('Victor', 'Kolis')
print(user.name, user.nickname)
