import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("Enter your journal entry: ")
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

        with open(self.filename, "a") as file:
            file.write(f"{timestamp}\n{entry}\n\n")

        print("Entry added successfully!")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                print(file.read())

        except FileNotFoundError:
            print("Error: The journal file does not exist. "
                  "Please add a new entry first.")

    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ")

        try:
            with open(self.filename, "r") as file:
                content = file.read()

            if keyword.lower() in content.lower():
                print("Matching entry found:")
                print(content)
            else:
                print(f"No entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("Error: The journal file does not exist.")

    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        confirm = input(
            "Are you sure you want to delete all entries? (yes/no): "
        )

        if confirm.lower() == "yes":
            os.remove(self.filename)
            print("All journal entries have been deleted.")
        else:
            print("Deletion cancelled.")

    @staticmethod
    def main():
        manager = JournalManager()

        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("Please select an option: \n")

            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                manager.add_entry()

            elif choice == '2':
                manager.view_entries()

            elif choice == '3':
                manager.search_entry()

            elif choice == '4':
                manager.delete_entries()

            elif choice == '5':
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            else:
                print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    JournalManager.main()