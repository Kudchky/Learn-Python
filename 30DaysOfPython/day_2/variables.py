company = "Coding For All"
sentence = 'You cannot end a sentence with because because because is a conjunction'

print(company.capitalize(), company.title(), company.swapcase())

print(company[company.find(" ") + 1: ])

print("Yes, word found" if company.find("Coding") >= 0 else "No, word not found")

print(company.replace("Coding", "Python"))

print(company.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

print("".join([word[0].upper() for word in company.split()]))

print(company.index("i"))

print(sentence.rindex("because"))

print(" ".join([el for el in sentence.split() if el != "because"]))