from functools import wraps


def make_pretty(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"I am {func.__name__} and I got decorated")
        output = func(*args, **kwargs)
        print()
        return output
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")
# ordinary = make_pretty(ordinary)  # ordinary = make_pretty.<locals>.inner


@make_pretty
def greet(name):
    print(f"Hello, {name}!")


@make_pretty
def compute(a, b, c=0):
    """Function that does a computation of three numbers"""
    return a * b + c


ordinary()

greet("Anna")
greet(name="John")

result = compute(20, 4, 4)
print("computation result:", result)

print(compute, compute.__name__, compute.__doc__)
