import random
import string

def generate_key():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    keys = chars.copy()
    random.shuffle(keys)
    return chars, keys

def encrypt_message(chars, keys, message):
    cipher_text = ""
    for letter in message:
        index = chars.index(letter)
        cipher_text += keys[index]
    return cipher_text

def decrypt_message(chars, keys, message):
    plain_text = ""
    for letter in message:
        index = keys.index(letter)
        plain_text += chars[index]
    return plain_text

def main():
    chars, keys = generate_key()

    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plain_text = input("Enter a message to encrypt: ")
            cipher_text = encrypt_message(chars, keys, plain_text)
            print(f"Original message: {plain_text}")
            print(f"Encrypted message: {cipher_text}")

        elif choice == '2':
            cipher_text = input("Enter a message to decrypt: ")
            plain_text = decrypt_message(chars, keys, cipher_text)
            print(f"Encrypted message: {cipher_text}")
            print(f"Decrypted message: {plain_text}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

