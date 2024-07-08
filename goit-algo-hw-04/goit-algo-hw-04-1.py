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




