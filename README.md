# Reading List Tracker

A Python script to track and manage your reading list from a markdown file. It categorizes books based on their status (read, currently reading, to read, did not finish) and provides useful statistics like the number of books read, currently reading, and more. It can also randomly pick a book from your "to read" list.

---

## Features

- **Categorize Books**: Automatically categorizes books into:
  - Read (`- [x]`)
  - Currently Reading (`- [/]`)
  - To Read (`- [ ]`)
  - Did Not Finish (`- [-]`)
- **Statistics**: Provides statistics like:
  - Total books
  - Books read
  - Books currently reading
  - Books to read
  - Books did not finish
- **Random Book Picker**: Randomly selects a book from your "to read" list.
- **Markdown File Support**: Reads from and processes a `READING LIST.md` file.

## Usage

### 1. Prepare Your Reading List
Create a markdown file named `READING LIST.md` in the project directory. Use the following format for each book:

```markdown
- [x] [[Book Title]] - Author  # Read
- [/] [[Book Title]] - Author  # Currently Reading
- [ ] [[Book Title]] - Author  # To Read
- [-] [[Book Title]] - Author  # Did Not Finish
```

### 2. Run the Script
Execute the script to process your reading list:
```bash
python reading_list.py
```

### 3. View the Output
The script will display:
- The book you're currently reading.
- Statistics about your reading progress.
- A randomly picked book from your "to read" list.

Example Output:
```
Currently reading: The Divine Comedy - Dante Alighieri
You read: 1 out of 4 books.
Did not finish: 1
Randomly picked next book: The 48 Laws of Power - Robert Greene
```

---

## Testing

The project includes unit tests to ensure the script works as expected. To run the tests:

1. Navigate to the project directory.
2. Run the tests:
   ```bash
   python -m unittest test_reading_list.py
   ```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

Do not contact me.
```