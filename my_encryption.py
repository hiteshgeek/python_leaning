alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_text(text, shift):
    encrypted_text = ""

    for i in text:
        target_index = (alphabets.index(i) + shift) % len(alphabets)
        encrypted_text += alphabets[target_index]

    return encrypted_text

def decrypt_text(text, shift):
    decrypted_text = ""
    for i in text:   
        target_index = (alphabets.index(i) + (shift * -1)) % len(alphabets)
        decrypted_text += alphabets[target_index]
        
    return decrypted_text