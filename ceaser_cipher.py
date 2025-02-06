import my_encryption

choice = input("Enter choice (encrypt, decrypt): \n")

while choice in ["encrypt", "decrypt"]:
    shift = input("Enter shift amount : \n")
    shift = int(shift)

    user_input = input("Enter text : \n")
    transformed = my_encryption.ceaser(user_input, shift, choice)
    print(f"Transformed text : {transformed}")

    choice = input("Enter choice (encrypt, decrypt): \n")

# entered_word = input("enter word to encrypt")
# print("Shifted Charactes : "+"".join(shifted_alphabets))

