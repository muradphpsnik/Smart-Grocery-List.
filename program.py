import datetime

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.shared_lists = []

class GroceryItem:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.purchased = False

class GroceryList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def update_item(self, item, new_name, new_category):
        item.name = new_name
        item.category = new_category

    def mark_as_purchased(self, item):
        item.purchased = True

    def mark_as_pending(self, item):
        item.purchased = False

    def get_purchased_items(self):
        return [item for item in self.items if item.purchased]

    def get_pending_items(self):
        return [item for item in self.items if not item.purchased]


class GroceryListManager:
    def __init__(self):
        self.lists = []
        self.users = []

    def create_list(self, name):
        new_list = GroceryList(name)
        self.lists.append(new_list)
        return new_list

    def delete_list(self, grocery_list):
        self.lists.remove(grocery_list)

    def share_list(self, grocery_list, user_email):
        user = self.find_user(user_email)
        if user:
            shared_list = grocery_list
            user.shared_lists.append(shared_list)
            print(f"Shared list '{grocery_list.name}' with {user.email}.")
        else:
            print("User not found.")

    def find_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_suggestions(self, user_preferences):
        pass

    def set_reminder(self, grocery_list, reminder_date):
        pass


# Function to display the available options
def display_options():
    print("Available options:")
    print("1. Create a new grocery list")
    print("2. Add item to a grocery list")
    print("3. Update an item in a grocery list")
    print("4. Mark an item as purchased")
    print("5. Mark an item as pending")
    print("6. Remove an item from a grocery list")
    print("7. Delete a grocery list")
    print("8. Share a grocery list with a user")
    print("9. View existing grocery lists")
    print("10. Quit the program")


# Function to handle the user's choice
def handle_choice(manager, choice):
    if choice == "1":
        name = input("Enter the name of the grocery list: ")
        manager.create_list(name)
        print(f"Grocery list '{name}' created.")
    elif choice == "2":
        list_name = input("Enter the name of the grocery list: ")
        item_name = input("Enter the name of the item: ")
        category = input("Enter the category of the item: ")
        grocery_list = find_list_by_name(manager, list_name)
        if grocery_list:
            item = GroceryItem(item_name, category)
            grocery_list.add_item(item)
            print(f"Item '{item_name}' added to '{list_name}'.")
        else:
            print("Grocery list not found.")
    elif choice == "3":
        list_name = input("Enter the name of the grocery list: ")
        item_name = input("Enter the name of the item to update: ")
        new_item_name = input("Enter the new name of the item: ")
        new_category = input("Enter the new category of the item: ")
        grocery_list = find_list_by_name(manager, list_name)
        if grocery_list:
            item = find_item_by_name(grocery_list, item_name)
            if item:
                grocery_list.update_item(item, new_item_name, new_category)
                print(f"Item '{item_name}' updated.")
            else:
                print("Item not found.")
        else:
            print("Grocery list not found.")
    elif choice == "4":
        list_name = input("Enter the name of the grocery list: ")
        item_name = input("Enter the name of the item to mark as purchased: ")
        grocery_list = find_list_by_name(manager, list_name)
        if grocery_list:
            item = find_item_by_name(grocery_list, item_name)
            if item:
                grocery_list.mark_as_purchased(item)
                print(f"Item '{item_name}' marked as purchased.")
            else:
                print("Item not found.")
        else:
            print("Grocery list not found.")
    elif choice == "5":
        list_name = input("Enter the name of the grocery list: ")
        item_name = input("Enter the name of the item to mark as pending: ")
        grocery_list = find_list_by_name(manager, list_name)
        if grocery_list:
            item = find_item_by_name(grocery_list, item_name)
            if item:
                grocery_list.mark_as_pending(item)
                print(f"Item '{item_name}' marked as pending.")
            else:
                print("Item not found.")
        else:
            print("Grocery list not found.")
    elif choice == "6":
        list_name = input("Enter the name of the grocery list: ")
        item_name = input("Enter the name of the item to remove: ")
        grocery_list = find_list_by_name(manager, list_name)
        if grocery_list:
            item = find_item_by_name(grocery_list, item_name)
            if item:
                grocery_list.remove_item(item)
                print(f"Item '{item_name}' removed from '{list_name}'.")
            else:
                print("Item not found.")
        else:
            print("Grocery list not found.")
    elif choice == "7":
        list_name = input("Enter the name of the grocery list to delete: ")
        grocery_list = find_list_by_name(manager, list_name)
        if grocery_list:
            manager.delete_list(grocery_list)
            print(f"Grocery list '{list_name}' deleted.")
        else:
            print("Grocery list not found.")
    elif choice == "8":
        list_name = input("Enter the name of the grocery list to share: ")
        user_email = input("Enter the email of the user to share with: ")
        grocery_list = find_list_by_name(manager, list_name)
        if grocery_list:
            manager.share_list(grocery_list, user_email)
        else:
            print("Grocery list not found.")
    elif choice == "9":
        view_existing_lists(manager)
    elif choice == "10":
        print("Exiting the program...")
        quit()
    else:
        print("Invalid choice. Please try again.")


# Function to find a grocery list by its name
def find_list_by_name(manager, name):
    for grocery_list in manager.lists:
        if grocery_list.name == name:
            return grocery_list
    return None


# Function to find an item in a grocery list by its name
def find_item_by_name(grocery_list, name):
    for item in grocery_list.items:
        if item.name == name:
            return item
    return None


# Function to display the existing grocery lists
def view_existing_lists(manager):
    print("Existing Grocery Lists:")
    if len(manager.lists) > 0:
        for grocery_list in manager.lists:
            print(f"- {grocery_list.name}")
            print("  Items:")
            if len(grocery_list.items) > 0:
                for item in grocery_list.items:
                    status = "Purchased" if item.purchased else "Pending"
                    print(f"  - {item.name} ({item.category}) - {status}")
            else:
                print("  No items found.")
    else:
        print("No grocery lists found.")


# Main program loop
def main():
    manager = GroceryListManager()
    while True:
        display_options()
        choice = input("Enter your choice (1-10): ")
        handle_choice(manager, choice)


# Run the program
if __name__ == "__main__":
    main()