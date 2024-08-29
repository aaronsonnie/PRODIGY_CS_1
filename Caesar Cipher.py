def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift - shift_base) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'encrypt':
        result = encrypt(message, shift)
    elif choice == 'decrypt':
        result = decrypt(message, shift)
    else:
        result = "Invalid choice. Please type 'encrypt' or 'decrypt'."
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
