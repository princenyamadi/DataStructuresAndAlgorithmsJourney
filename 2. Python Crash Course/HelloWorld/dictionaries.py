customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True

}

print(customer)
print(customer["name"])
print(customer["age"])
print(customer["is_verified"])
# .get method does not return a runtime error if the key is not found
print(customer.get("birthdate", "Jan 1 1980"))


phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"


}

for ch in phone:
    output = ""
    output += digits_mapping.get(ch, "!") + " "

print(output)
