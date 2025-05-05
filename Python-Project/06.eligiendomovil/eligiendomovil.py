input_user = input("\nWhat mobile wants: \n"
                    "1) ANDROID\n"
                    "2) IOS\n"
                    ">> "
                   )
if input_user == "1":
    has_money = input("¿Do you have money [Y/N]: ").upper()

    if has_money == "N":
        print("You can buy your Chinese Android 100 EUR")
    elif has_money == "Y":
        camera = input("You care about the mobile camera? [Y/N]: ").upper()
        if camera == "Y":
            print("Buy Google Pixel Super Camera")
        elif camera == "N":
            print("Buy an android quality price")
        else:
            print("Write a correct answer Y or N")
    else:
        print("Write a correct option Y or N")
elif input_user == "2":
    has_money = input("¿Do you have money [Y/N]: ").upper()

    if has_money == "Y":
        print("Buy the iPhone Ultra Pro Max")
    elif has_money == "N":
        print("Buy a second -hand iPhone")
    else:
        print("Enter a correct answer Y or N")
else:
    print("Enter a correct answer 1 o 2")




