import os                                                                                #1
import json

# Define the global constant for the dictionary JSON file
FILE_NAME = "dictionary.json"


def load_dictionary():                                                                  #2
    # Reads the JSON file and deserializes it into a Python dictionary.#
    # Check if the file exists; if not, create an empty JSON file
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
        return {}

    # Open and deserialize JSON file to Python dictionary                               #3
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # Return empty dictionary if file is corrupted or empty
            return {}


def save_dictionary(dictionary):
    # Serializes the Python dictionary and writes it to the JSON file.#
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)


def save_translation(lang_pair, word, translation):                                    #4
    # Adds a new word translation to the dictionary and saves it.#
    dictionary = load_dictionary()

    if lang_pair not in dictionary:
        dictionary[lang_pair] = {}

    dictionary[lang_pair][word.lower()] = translation
    save_dictionary(dictionary)


def translate_word(lang_pair, lang_name):                                             #5
    print(f"\n--- {lang_name} ---")

    # Get word from the user and strip extra spaces
    word = input("Enter a word or short phrase: ").strip()

    # Validate that the input is not empty
    if word == "":
        print("Error: Word cannot be empty!")
        input("\nPress Enter to continue...")
        return

    # Load the current dictionary from the JSON file                                  #6
    dictionary = load_dictionary()

    # Check if the language pair exists and if the word is in that specific dictionary    #7
    if lang_pair in dictionary and word.lower() in dictionary[lang_pair]:
        result = dictionary[lang_pair][word.lower()]
        print(f"Translation: {result}")
    else:
        # If word is not found, prompt the user to add it
        print(f"'{word}' was not found in the dictionary.")
        add_new = input("Would you like to add it? (yes/no): ").strip().lower()

        # Handle user confirmation                                                  #8
        if add_new == "yes" or add_new == "y":
            new_translation = input(f"Enter translation for '{word}': ").strip()

            # Ensure the new translation is not empty before saving
            if new_translation != "":
                save_translation(lang_pair, word, new_translation)
                print("Success: Word added to dictionary!")
            else:
                print("Error: Translation cannot be empty.")

    # Wait for user to press Enter before returning to the main menu           #9
    input("\nPress Enter to continue...")


def delete_word():
    print("\n--- Delete Word ---")
    print("1. English to Georgian")
    print("2. Georgian to English")
    print("3. French to Georgian")
    print("4. Georgian to French")

    choice = input("Select language pair (1-4): ").strip()
    lang_map = {"1": "en-ka", "2": "ka-en", "3": "fr-ka", "4": "ka-fr"}

    if choice not in lang_map:
        print("Invalid choice.")
        input("\nPress Enter to continue...")
        return

    lang_pair = lang_map[choice]
    word = input("Enter word to delete: ").strip()

    if word == "":
        print("Error: Word cannot be empty!")
        input("\nPress Enter to continue...")
        return

    dictionary = load_dictionary()

    # Check if word exists in specified language dictionary and delete it              #10
    if lang_pair in dictionary and word.lower() in dictionary[lang_pair]:
        del dictionary[lang_pair][word.lower()]
        save_dictionary(dictionary)
        print(f"Success: '{word}' deleted from dictionary!")
    else:
        print(f"'{word}' was not found in the dictionary.")

    # Wait for user to press Enter before returning to the main menu                 #11
    input("\nPress Enter to continue...")


def show_all_words():
    print("\n--- All Dictionary Words ---")
    dictionary = load_dictionary()

    if not dictionary:
        print("Dictionary is empty.")
    else:
        has_words = False
        for lang_pair, words in dictionary.items():
            if words:
                has_words = True
                print(f"\n[Language Pair: {lang_pair}]")
                for word, translation in words.items():
                    print(f"  • {word} -> {translation}")

        if not has_words:
            print("Dictionary is empty.")

    input("\nPress Enter to continue...")


def main():
    # Infinite loop to keep the menu active until the user decides to exit
    while True:
        print("\n==============================")
        print("         TRANSLATOR           ")
        print("==============================")
        print("1. English to Georgian")
        print("2. Georgian to English")
        print("3. French to Georgian")
        print("4. Georgian to French")
        print("5. Delete a Word")
        print("6. Show All Words")
        print("7. Exit")
        print("==============================")

        # Get menu choice from user
        choice = input("Select an option (1-7): ").strip()

        # Route the choice to the correct translation configuration
        if choice == "1":
            translate_word("en-ka", "English to Georgian")
        elif choice == "2":
            translate_word("ka-en", "Georgian to English")
        elif choice == "3":
            translate_word("fr-ka", "French to Georgian")
        elif choice == "4":
            translate_word("ka-fr", "Georgian to French")
        elif choice == "5":
            delete_word()
        elif choice == "6":
            show_all_words()
        elif choice == "7":
            print("Goodbye!")
            break  # Exit the while loop and terminate the program
        else:
            print("Invalid choice. Please select a valid number.")
            input("\nPress Enter to continue...")


# Ensure the main function runs only when the script is executed directly             #12
if __name__ == "__main__":
    main()
