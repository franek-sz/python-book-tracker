from random import choice

STATUS_READ = "- [x] "
STATUS_READING = "- [/] "
STATUS_DNF = "- [-] "
STATUS_TO_READ = "- [ ] "
TO_REMOVE = ["- [x] ", "- [/] ", "- [-] ", "- [ ] ", "[[", "]]", "*", "\n"]

def clean_line(line):
    for char in TO_REMOVE:
        line = line.replace(char, "")
    return line.strip()

def process_line(line, counters, books_to_read):
    if line.startswith(STATUS_READ):
        counters["read"] += 1
        counters["total"] += 1
    elif line.startswith(STATUS_READING):
        counters["total"] += 1
        cleaned_line = clean_line(line)
        counters["currently_reading"] = cleaned_line
    elif line.startswith(STATUS_DNF):
        counters["dnf"] += 1
        counters["total"] += 1
    elif line.startswith(STATUS_TO_READ):
        counters["to_read"] += 1
        counters["total"] += 1
        cleaned_line = clean_line(line)
        books_to_read.append(cleaned_line)

def main():
    counters = {
        "read": 0,
        "dnf": 0,
        "to_read": 0,
        "total": 0,
        "currently_reading": None,
    }

    books_to_read = []

    try:
        with open("READING LIST.md", "r", encoding="utf-8") as file:
            for line in file:
                process_line(line, counters, books_to_read)

        if counters["currently_reading"]:
            print(f"Currently reading: {counters['currently_reading']}")
        else:
            print("You are not currently reading any book.")

        print(f"You read: {counters['read']} out of {counters['total']} books.")
        print(f"Did not finish: {counters['dnf']}")
        if books_to_read:
            print(f"Randomly picked next book: {choice(books_to_read)}")
        else:
            print("No books to read in the list.")

    except FileNotFoundError:
        print("Error: The file 'READING LIST.md' was not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()