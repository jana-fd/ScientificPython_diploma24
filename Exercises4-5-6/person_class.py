class Person:
    def __init__(self, first_name = '',last_name = '',age = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return 'Full name: ' + self.first_name.capitalize() + ' ' + self.last_name.capitalize()

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


if __name__ == "__main__":
    p1 = Person('Jana', 'Fakher Eddine', 24)
    print(p1.full_name())
    print(p1.is_adult())
