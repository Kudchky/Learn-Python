signs = [".", ",", "!", "¡", "?", "¿"]
phrase = input("Enter your phrase: ").lower()

result = len(set("".join([l for l in phrase if l not in signs]).split()))

print(result)


