

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
