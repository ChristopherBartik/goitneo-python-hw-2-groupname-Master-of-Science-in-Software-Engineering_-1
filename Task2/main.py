class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        # You can add phone-specific validation here

class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        # You can add email-specific validation here

class Record:
    def __init__(self, name: Name, phones=None, emails=None):
        self.name = name  # Required field
        self.phones = phones if phones is not None else []  # Optional, can have multiple
        self.emails = emails if emails is not None else []  # Optional, can have multiple

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)

    def add_email(self, email: Email):
        self.emails.append(email)

    def remove_email(self, email: Email):
        self.emails.remove(email)

class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record: Record):
        self.records[record.name.value] = record

    def delete_record(self, name: str):
        if name in self.records:
            del self.records[name]

    def find_record(self, name: str):
        return self.records.get(name, None)

    # Example of a search by criteria (name in this case)
    def search_by_name(self, name: str):
        return [record for record_name, record in self.records.items() if name in record_name]

if __name__ == "__main__":

    # Creating some dummy data
    address_book = AddressBook()

    # Adding a record for John Doe with two phone numbers and one email
    john = Record(Name("John Doe"), [Phone("1234567890"), Phone("0987654321")], [Email("john.doe@example.com")])
    address_book.add_record(john)

    # Adding a record for Jane Doe with one phone number
    jane = Record(Name("Jane Doe"), [Phone("5555555555")])
    address_book.add_record(jane)

def display_address_book(abook):
    for name, record in abook.records.items():
        print(f"Name: {name}")
        for phone in record.phones:
            print(f"Phone: {phone.value}")
        for email in record.emails:
            print(f"Email: {email.value}")
        print("-----")

# Display the address book with dummy data
display_address_book(address_book)