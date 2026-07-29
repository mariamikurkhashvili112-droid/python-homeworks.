import json                                                                       #1
import os


# Represents an individual book object                                            #2
class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Helper function to convert a Book object into a dictionary for JSON serialization        #3
def book_serializer(book):
    return {"title": book.title, "author": book.author, "year": book.year}


# Helper function to convert a dictionary back into a Book object for JSON deserialization
def book_deserializer(item):
    return Book(item["title"], item["author"], item["year"])


# Manages book storage, retrieval, and file persistence                        #4
class BookManager:

    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books_list = []
        self.load_books()

    # Reads JSON file and deserializes dictionaries into Book objects         #5
    def load_books(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.books_list = [
                        book_deserializer(item) for item in data
                    ]
            except (json.JSONDecodeError, Exception):
                self.books_list = []
        else:
            self.books_list = []

    # Serializes the Book objects and writes them to JSON
    def save_books(self):
        serialized_list = []
        for book in self.books_list:
            serialized_list.append(book_serializer(book))

        with open(self.filename, "w") as f:
            json.dump(serialized_list, f, indent=4)

    # Adds a newly created book, checks for duplicates, and saves to file           #6
    def add_book(self, book):
        if isinstance(book, Book):
            for existing_book in self.books_list:
                if existing_book.title.lower() == book.title.lower():
                    print(
                        f"\nNotice: The book '{book.title}' is already in the system! It will not be added again."
                    )
                    return

            self.books_list.append(book)
            self.save_books()
            print(f"\nSuccess! Book '{book.title}' has been added.")
        else:
            print("\nError: Only Book objects can be added.")

    # Displays all books currently in the system                #7
    def view_all_books(self):
        if not self.books_list:
            print("\nNo books available in the system.")
            return

        print("\n--- List of All Books ---")
        for index, book in enumerate(self.books_list, start=1):
            print(f"{index}. {book.display_details()}")
        print("-------------------------")

    # Filters and searches the list for a specific book by title, author, or release year          #8
    def search_books(self, search_term):
        search_term_lower = search_term.lower()
        print(f"\n--- Search Results for '{search_term}' ---")
        found_books = []

        for book in self.books_list:
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


# Main function to run the Console Application UI                    #9
def main():
    manager = BookManager("books.json")

    while True:
        print("\n=== BOOK MANAGEMENT SYSTEM ===")
        print("1. Add a new Book")
        print("2. View all Books")
        print("3. Search Books")
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

            # Author validation                           #10
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
                manager.search_books(search_term)
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
