import os
import csv
import json

def load_scores(path: str) -> list[tuple[str, int]]:
    records = []
    if not os.path.exists(path):
        print("File not found. Starting fresh.")
        return records
    try:
        if path.endswith(".csv"):
            with open(path, mode='r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 2:
                        name, score = row
                        records.append((name, int(score)))
        elif path.endswith(".json"):
            with open(path, 'r') as f:
                data = json.load(f)
                records = [(item['name'], item['score']) for item in data]
        else:
            print("Unsupported file type.")
    except Exception as e:
        print(f"Failed to load file: {e}")
    return records

def add_score(records: list[tuple[str, int]], name: str, score: int) -> None:
    records.append((name, score))

def save_scores(path: str, records: list[tuple[str, int]]) -> None:
    try:
        if path.endswith(".csv"):
            with open(path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(records)
        elif path.endswith(".json"):
            with open(path, 'w') as f:
                json.dump([{'name': name, 'score': score} for name, score in records], f)
        else:
            print("Unsupported file type.")
    except Exception as e:
        print(f"Error saving file: {e}")

def top_n(records: list[tuple[str, int]], n: int) -> list[tuple[str, int]]:
    return sorted(records, key=lambda x: x[1], reverse=True)[:n]

def delete_all_scores(path: str) -> None:
    confirm = input("Are you sure you want to delete all scores? (yes/no): ")
    if confirm.lower() == "yes":
        save_scores(path, [])
        print("All scores deleted.")
    else:
        print("Cancelled.")

def main():
    filepath = "scores.csv"
    records = load_scores(filepath)

    while True:
        print("\nScore Keeper Menu")
        print("1. Show Top N Scores")
        print("2. Add New Score")
        print("3. Delete All Scores")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            try:
                n = int(input("How many top scores to show? "))
                top = top_n(records, n)
                print("\nTop Scores:")
                for name, score in top:
                    print(f"{name}: {score}")
            except ValueError:
                print("Invalid number. Try again.")

        elif choice == "2":
            name = input("Enter name: ").strip()
            try:
                score = int(input("Enter score: "))
                add_score(records, name, score)
                save_scores(filepath, records)
                print("Score added.")
            except ValueError:
                print("Invalid score. Must be a number.")

        elif choice == "3":
            delete_all_scores(filepath)
            records = []

        elif choice == "4":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
