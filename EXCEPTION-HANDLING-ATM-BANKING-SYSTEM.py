from typing import Generic, TypeVar

# Create a type variable
T = TypeVar('T')


# Generic Storage class
class Storage(Generic[T]):
    def __init__(self):
        self.item = None

    def store(self, item: T):
        self.item = item

    def retrieve(self) -> T:
        return self.item


# Demonstration with an integer
integer_storage = Storage[int]()
integer_storage.store(100)
print("Integer:", integer_storage.retrieve())

# Demonstration with a string
string_storage = Storage[str]()
string_storage.store("Smart Warehouse")
print("String:", string_storage.retrieve())

# Demonstration with a list
list_storage = Storage[list]()
list_storage.store(["Laptop", "Printer", "Scanner"])
print("List:", list_storage.retrieve())