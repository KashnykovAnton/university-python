import sys
import os

def parse_log_line(line: str) -> dict:
    try:
        parts = line.split(" ", 3)
        if len(parts) < 4:
            raise ValueError(f"Invalid log line format: '{line}'")

        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3].strip(),
        }
    except ValueError as e:
        raise ValueError(f"Error parsing log line: {e}")

def load_logs(file_path: str) -> list:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            logs.append(parse_log_line(line.strip()))
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
        # solution in one stroke - counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in counts:
        print(f"{level:<16} | {counts[level]}")

def main():
    if len(sys.argv) < 2:
        print("At least one argument is required!")
        print("Usage: python main.py <log_file_path> [log_level]")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(log_file_path)
        
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        
        if log_level:
            filtered_logs = filter_logs_by_level(logs, log_level)
            print(f"\nДеталі логів для рівня '{log_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
