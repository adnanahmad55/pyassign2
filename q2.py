def read_lines(filename: str) -> list[str]:
   
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return []

def main():
    filename = input("Enter the file name: ")
    lines = read_lines(filename)
    print(f"Total lines: {len(lines)}")

if __name__ == "__main__":
    main()
