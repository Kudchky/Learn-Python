user_name = input("Enter you username: ")

if len(user_name) > 12:
    print("Username is no more than 12 characters")
elif user_name.count(" ") > 0:
    print("Username must not contain space")
elif not user_name.isalpha():
    print("Username must not contain digits")
else:
    print(f"Username {user_name} validated")