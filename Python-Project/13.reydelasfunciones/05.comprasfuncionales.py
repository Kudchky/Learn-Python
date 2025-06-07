EXIT = "exit"
SHOW_LIST = "show"

our_list = ["banana", "potato", "oil", "cheese", "eggs", "butter", "orange", "honey"]

def ask_item():
    return input(f"Enter a item [{EXIT} to close or {SHOW_LIST} to see list of available products]: ")

def save_file(list_items):
    file = open("shops.txt", "w")
    file.write("\n".join(list_items))
    file.close()

def main():
    shopping_list = []


    while True:
        input_user = ask_item().lower().strip()

        if input_user == EXIT:
            break
        elif input_user == SHOW_LIST:
            print("Available items: ", ", ".join(our_list))
        elif input_user in our_list:
            our_list.remove(input_user)
            shopping_list.append(input_user)
            print(f"\n{input_user.capitalize()} added to the shopping list\n")
        else:
            print(f"\n{input_user.capitalize()} is not available to add\n")


    save_file(shopping_list)
    print("Shopping list saved to shops.txt. Bye!")


if __name__ == "__main__":
    main()
