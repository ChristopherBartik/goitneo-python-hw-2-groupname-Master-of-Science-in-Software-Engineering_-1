from record import Record
from field import Name


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: Name):
        if isinstance(name, str):
            name = Name(name)
            # Now proceed assuming 'name' is a Name object
        return self.data.get(name.value, None)

    def delete(self, name: Name):
        if name.value in self.data:
            del self.data[name.value]
