from datetime import date


class Person:
    count = 0  # class attributes
    MIN_YEAR = 1900

    def __init__(self, name, date_of_birth: date):
        self.name = name  # instance attributes
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: date):
        if value.year < self.MIN_YEAR:
            raise ValueError("invalid date of birth")
        self._date_of_birth = value

    @property
    def age(self):
        return self.years_since(self._date_of_birth)

    def __str__(self):
        return f"<{__name__}.{self.__class__.__name__} name={self.name} "\
               f"date_of_birth={self.date_of_birth}>"

    def __lt__(self, other):
        return self._date_of_birth > other.date_of_birth

    def __le__(self, other):
        return self._date_of_birth >= other.date_of_birth

    @classmethod
    def _increment_count(cls):
        cls.count += 1

    @staticmethod
    def years_since(date_obj: date):
        today = date.today()
        years = today.year - date_obj.year
        if (today.month, today.day) < (date_obj.month, date_obj.day):
            years -= 1
        return years


# everything under this condition will be skipped at import
if __name__ == "__main__":
    p1 = Person("Anna", date(2001, 5, 1))
    print(p1.name, p1.date_of_birth)
    print(str(p1), repr(p1))
    print(Person.count, p1.count, p1.count is Person.count)

    p2 = Person("John", date(1987, 6, 23))
    print(p2.name)

    try:
        p2.date_of_birth = date(1887, 6, 23)
    except ValueError as ex:
        print(ex)

    print(str(p2.date_of_birth), repr(p1.date_of_birth))

    print(f"{p1.name} is younger than {p2.name}: {p1 < p2}")

    print(p1.__dict__)

    print("Person count:", Person.count)

    print(Person.years_since(date(1918, 12, 1)))
    print(f"{p1.name} is {p1.age} years old.")
