class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct, **kwds):
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct, **kwds)

    def __call__(cls, *args, **kwargs):
        print(f"Metaclass called with args={args}, kwargs={kwargs}")
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    print(type(MyClass))
    my_obj = MyClass(100, y=1)
