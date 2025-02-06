import my_encryption

choice = input("Enter choice (encrypt, decrypt): \n")

while choice in ["encrypt", "decrypt"]:
    shift = input("Enter shift amount : \n")
    shift = int(shift)

    user_input = input("Enter text : \n")
    if choice == "encrypt":       
        encrypted_text = my_encryption.encrypt_text(user_input, shift)
        print(f"Encrypted text : {encrypted_text}")
    elif choice == "decrypt":  
        decrypted_text = my_encryption.decrypt_text(user_input, shift)
        print(f"Decrypted text : {decrypted_text}")
    else:
        break;

    choice = input("Enter choice (encrypt, decrypt): \n")

# entered_word = input("enter word to encrypt")
# print("Shifted Charactes : "+"".join(shifted_alphabets))

