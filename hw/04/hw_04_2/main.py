path_to_file = "hw/04/hw_04_2/cats.txt"

def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines()]

        if not lines:
            print("The file is empty.")
            return []

        cats = []

        for line in lines:
            parts = line.split(",")
            if len(parts) < 3:
                raise ValueError(f"Invalid line format: {line}")
            cats.append({
                "id": parts[0],
                "name": parts[1],
                "age": parts[2]
            })
        
        return cats
    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0)

cats_info = get_cats_info(path_to_file)
print(cats_info)