class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class user:
    def __init__(self, name):
        self.name = name

class User(user, metaclass=Singleton):
    pass

if __name__ == '__main__':
    a = User('joao')
    b = User('maria')
    c = User('joana')
    print(a.name)
    print(b.name)
    print(c.name)
    