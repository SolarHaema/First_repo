import re
import pickle
from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError(f"Phone number {value} is not valid. It must be 10 digits.")
        super().__init__(value)

    def validate_phone(self, value):
        return bool(re.match(r"^\d{10}$", value))

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError(f"Phone number {phone} not found.")

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.phones[self.phones.index(phone_obj)] = Phone(new_phone)
        else:
            raise ValueError(f"Phone number {old_phone} not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_data()

    def add_record(self, record):
        self.data[record.name.value] = record
        self.save_data()

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            self.save_data()
        else:
            raise KeyError(f"Name {name} not found.")

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now()
        for record in self.data.values():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                bday_this_year = bday.replace(year=today.year)
                if 0 <= (bday_this_year - today).days <= 7:
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": bday_this_year.strftime("%d.%m.%Y")
                    })
        return upcoming_birthdays

    def save_data(self):
        with open('address_book.pkl', 'wb') as file:
            pickle.dump(self.data, file)

    def load_data(self):
        try:
            with open('address_book.pkl', 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            self.data = {}

    def __str__(self):
        result = "\n".join(str(record) for record in self.data.values())
        return result if result else "No contacts found."

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError as ve:
            return str(ve)
        except IndexError:
            return "Provide both name and phone number."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    record = contacts.find(name)
    if record:
        record.add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, old_phone, new_phone = args
    record = contacts.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise KeyError("Name not found.")

@input_error
def show_phone(args, contacts):
    name = args[0]
    record = contacts.find(name)
    if record:
        return str(record)
    else:
        raise KeyError("Name not found.")

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    record = contacts.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError("Name not found.")

@input_error
def get_upcoming_birthdays(contacts):
    birthdays = contacts.get_upcoming_birthdays()
    if birthdays:
        return "\n".join([f"{b['name']}: {b['birthday']}" for b in birthdays])
    else:
        return "No upcoming birthdays."

def show_all(contacts):
    return str(contacts)

def main():
    contacts = AddressBook()
    print("""
    Welcome to the assistant bot!
          
    Available commands:
          
    - add [name] [phone]: Add a new contact;
    - change [name] [old phone] [new phone]: Change the phone number of an existing contact;
    - phone [name]: Show the phone number of a contact;
    - birthday [name] [birthday]: Add a birthday to a contact;
    - upcoming: Show contacts with upcoming birthdays;
    - all: Show all contacts;
    - close/exit: Exit the bot.
    """)
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "birthday":
            print(add_birthday(args, contacts))
        elif command == "upcoming":
            print(get_upcoming_birthdays(contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
