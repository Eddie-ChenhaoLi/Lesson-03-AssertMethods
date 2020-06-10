class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def get_full_name(self):
        return '{} {}'.format(self.first, self.last)

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
