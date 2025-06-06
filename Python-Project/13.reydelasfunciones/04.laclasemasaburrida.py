import random

def longest_string(*args):
    if not args:
        return None

    greater = args[0]
    for el in args:
        if len(greater) <= len(el):
            greater = el

    return greater

def  adding_numbers(numbers_list):
    result = 0
    for el in numbers_list:
        result += el

    return result

def even_odd_number(number):
    return number % 2 != 0

def ask_something():
    option = input('''Are you sure or not? [Enter option 1 or 2]
        1) Yes, I am sure.
        2) No, I am not sure. >> ''')

    if option == str(1):
        return True
    else:
        return False

def convert_uppercase(text):
    result = ""
    for char in text:
        ascii_val = ord(char)
        if ord("a") <= ascii_val <= ord("z"):
            result += chr(ascii_val - 32)
        else:
            result += char

    return result

def guess_number(number):
    option = -1

    while number != option:
        try:
            option = int(input("Guess a number between 1 to 100: >> "))

            if not 0 < option <= 100:
                print("Incorrect number, value between 1 to 100")
                continue

            if option < number:
                print("Try a higher number!")
            elif option > number:
                print("Try a lower number")
        except ValueError:
            print("Enter an entire number")

    print("You found the number")

list_shop = ["apple", "milk", "eggs"]
def add_item():
    item = input("Enter new item to the shopping list: >> ").strip().lower()

    if item in list_shop:
        print(f"Item: {item} is already on the purchase list")
    else:
        list_shop.append(item)
        print(f"Item: {item} added to the purchase list")

    return f"Current list: {", ".join(list_shop)}"

if __name__ == "__main__":

    print(longest_string("hola", "como", "estas", "Fernando"))
    print(adding_numbers([1, 2, 3, 4, 5]))
    print(even_odd_number(24))
    print(ask_something())
    print(convert_uppercase("Hola como estas"))
    guess_number(109)
    guess_number(random.randint(1, 100))
    print(add_item())