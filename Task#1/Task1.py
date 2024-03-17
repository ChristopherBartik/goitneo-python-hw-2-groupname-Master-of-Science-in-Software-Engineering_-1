def input_error(func):
    def inner(*args, **kwargs):  # Adjusted to *args and **kwargs for general purpose
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input format. Please enter the command correctly."
    return inner