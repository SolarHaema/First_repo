from pathlib import Path

def total_salary(path):
    total = 0
    count = 0
    
    try:
        file_path = Path(path)
        
        if not file_path.exists():
            print(f"File not found: {file_path}")
            return (0, 0.0)
        
        with file_path.open('r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 2:
                        _, salary = parts
                        total += int(salary)
                        count += 1
        
        if count == 0:
            return (0, 0.0)
        
        average = total / count
        return (total, average)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0.0)

file_path = 'E:/mygame/hm4.txt'
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}")
print(f"Середня сума заробітної плати: {average:.2f}")




def get_cats_info(path):
    cats_info = []
    
    try:
        file_path = Path(path)
        
        if not file_path.exists():
            print(f"File not found: {file_path}")
            return cats_info
        
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        try:
                            age = int(age)
                            cat_info = {"id": cat_id, "name": name, "age": age}
                            cats_info.append(cat_info)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cats_info

file_path = 'E:/mygame/cats.txt'
cats = get_cats_info(file_path)
for cat in cats:
    print(cat)




def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Need name and number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Nee dname and number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Enter a name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts available."
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
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
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
