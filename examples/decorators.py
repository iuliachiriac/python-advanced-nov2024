from functools import wraps


def make_pretty(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"I am {func.__name__} and I got decorated")
        output = func(*args, **kwargs)
        print()
        return output
    return inner


def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            output = None
            for _ in range(num_times):
                output = func(*args, **kwargs)
            return output
        return wrapper
    return decorator_repeat


@repeat(3)
@make_pretty
def ordinary():
    print("I am ordinary")
# ordinary = make_pretty(ordinary)  # ordinary = make_pretty.<locals>.inner
# ordinary = repeat(3)(ordinary) ~ decorator_repeat(ordinary)


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

print(ordinary, ordinary.__name__)
print(compute, compute.__name__, compute.__doc__)
