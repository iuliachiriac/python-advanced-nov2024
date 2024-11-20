from datetime import date


class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"<{__name__}.{self.__class__.__name__} name={self.name} "\
               f"date_of_birth={self.date_of_birth}>"

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def __le__(self, other):
        return self.date_of_birth >= other.date_of_birth


# everything under this condition will be skipped at import
if __name__ == "__main__":
    p1 = Person("Anna", date(2001, 5, 1))
    print(p1.name, p1.date_of_birth)
    print(str(p1), repr(p1))

    p2 = Person("John", date(1987, 6, 23))
    print(p2.name)

    print(str(p1.date_of_birth), repr(p1.date_of_birth))

    print(f"{p1.name} is younger than {p2.name}: {p1 < p2}")

    print(p1.__dict__)
