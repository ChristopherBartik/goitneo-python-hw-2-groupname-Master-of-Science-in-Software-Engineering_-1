from copy import deepcopy, copy
import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):

    def __init__(self, value):
        if not self.validate(value):
            raise ValueError(f"Phone number {value} is invalid. Must be 10 digits.")
        super().__init__(value)

    @staticmethod
    def validate(phone_number):
        return bool(re.match(r'^\d{10}$', phone_number))



