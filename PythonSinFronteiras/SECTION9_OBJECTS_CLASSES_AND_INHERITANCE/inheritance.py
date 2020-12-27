class User:
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname

    def greeting(self):
        print('Hi, my name is:', self.name, self.nickname)


class Admin(User):
    def super_greeting(self):
        print('HOLA!! ME LLAMO', self.name, 'Y SOY ADMINISTRADOR')


admin = Admin('VICTOR', 'KOLIS')
admin.greeting()
admin.super_greeting()
