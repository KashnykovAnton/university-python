path_to_file = "hw/04/hw_04_1/salary.txt"

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines()]

        if not lines:
            print("The file is empty.")
            return (0, 0)

        salaries = []
        for line in lines:
            salary = int(line.split(",")[1])
            salaries.append(salary)
        
        total_salary = sum(salaries)
        average_salary = total_salary // len(salaries)

        return (total_salary, average_salary)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0)


total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")