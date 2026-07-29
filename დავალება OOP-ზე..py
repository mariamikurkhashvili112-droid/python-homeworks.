import json          #1
import os


# Base class for generic library items with encapsulated attributes    #2
class LibraryItem:

    def __init__(self, title, author):
        self._title = title
        self._author = author

    # Encapsulated getter for title
    @property
    def title(self):
        return self._title

    # Encapsulated setter for title
    @title.setter
    def title(self, value):
        if not value or not str(value).strip():
            raise ValueError("Title cannot be empty.")
        self._title = value.strip()

    # Encapsulated getter for author
    @property
    def author(self):
        return self._author

    # Encapsulated setter for author
    @author.setter
    def author(self, value):
        if not value or not str(value).strip():
            raise ValueError("Author cannot be empty.")
        self._author = value.strip()


# Child class representing a Book item (inherits from LibraryItem)        #3
class Book(LibraryItem):

    def __init__(self, title, author, year):
        super().__init__(title, author)
        self._year = year

    # Encapsulated getter for year
    @property
    def year(self):
        return self._year

    # Encapsulated setter for year
    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Release year must be a positive integer.")
        self._year = value

    def display_details(self):                #4
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Helper function to convert a Book object into a dictionary for JSON serialization      #5
def book_serializer(book):
    return {"title": book.title, "author": book.author, "year": book.year}


# Helper function to convert a dictionary back into a Book object for JSON deserialization
def book_deserializer(item):
    return Book(item["title"], item["author"], item["year"])


# Manages book storage, retrieval, and file persistence       #6
class BookManager:

    def __init__(self, filename="books.json"):
        self._filename = filename
        self._books_list = []
        self.load_books()

    @property
    def filename(self):
        return self._filename

    @property
    def books_list(self):
        return self._books_list

    # Reads JSON file and deserializes dictionaries into Book objects      #7
    def load_books(self):
        if os.path.exists(self._filename):
            try:
                with open(self._filename, "r") as f:
                    data = json.load(f)
                    self._books_list = [
                        book_deserializer(item) for item in data
                    ]
            except (json.JSONDecodeError, Exception):
                self._books_list = []
        else:
            self._books_list = []

    # Serializes the Book objects and writes them to JSON
    def save_books(self):
        serialized_list = []
        for book in self._books_list:
            serialized_list.append(book_serializer(book))

        with open(self._filename, "w") as f:
            json.dump(serialized_list, f, indent=4)

    # Adds a newly created book, checks for duplicates, and saves to file       #8
    def add_book(self, book):
        if isinstance(book, Book):
            for existing_book in self._books_list:
                if existing_book.title.lower() == book.title.lower():
                    print(
                        f"\nNotice: The book '{book.title}' is already in the system! It will not be added again."
                    )
                    return

            self._books_list.append(book)
            self.save_books()
            print(f"\nSuccess! Book '{book.title}' has been added.")
        else:
            print("\nError: Only Book objects can be added.")

    # Displays all books currently in the system        #9
    def view_all_books(self):
        if not self._books_list:
            print("\nNo books available in the system.")
            return

        print("\n--- List of All Books ---")           #10
        for index, book in enumerate(self._books_list, start=1):
            print(f"{index}. {book.display_details()}")
        print("-------------------------")

    # Filters and searches the list for a specific book by title, author, or release year    #11
    def search_book_by_title(self, search_term):
        search_term_lower = search_term.lower()
        print(f"\n--- Search Results for '{search_term}' ---")
        found_books = []

        for book in self._books_list:
            if (
                search_term_lower in book.title.lower()
                or search_term_lower in book.author.lower()
                or search_term_lower == str(book.year)
            ):
                found_books.append(book)

        if found_books:
            for book in found_books:
                print(book.display_details())
        else:
            print("No books found matching that criteria.")
        print("-----------------------------------")


# Main function to run the Console Application UI     #12
def main():
    manager = BookManager("books.json")

    while True:
        print("\n=== BOOK MANAGEMENT SYSTEM ===")
        print("1. Add a new Book")
        print("2. View all Books")
        print("3. Search Book by Title")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            # Title validation
            while True:
                title = input("Enter Book Title: ").strip()
                if title == "":
                    print("Error: Title cannot be empty. Please try again.")
                else:
                    break

            # Author validation
            while True:
                author = input("Enter Book Author: ").strip()
                if author == "":
                    print("Error: Author cannot be empty. Please try again.")
                else:
                    break

            # Year validation
            while True:
                year_str = input("Enter Release Year: ").strip()
                if not year_str.isdigit():
                    print(
                        "Error: Release year must be numeric (e.g., 2023). Please try again."
                    )
                else:
                    year = int(year_str)
                    break

            new_book = Book(title, author, year)
            manager.add_book(new_book)

        elif choice == "2":
            manager.view_all_books()

        elif choice == "3":
            search_term = input(
                "Enter title, author, or year to search for: "
            ).strip()
            if search_term != "":
                manager.search_book_by_title(search_term)
            else:
                print("Search term cannot be empty.")

        elif choice == "4":
            print("Exiting Book Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
