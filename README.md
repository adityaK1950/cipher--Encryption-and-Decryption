# Random Key Encryption and Decryption
This Python script demonstrates a simple encryption and decryption process using a randomly generated key. The program allows users to encrypt and decrypt messages.

## Features
1. Encrypt a Message: Users can input a message, and the program will encrypt it using a randomly generated key.

2. Decrypt a Message: Users can input an encrypted message, and the program will decrypt it using the same key.

3. Menu Driven: The program provides a menu for users to choose between encryption, decryption, or exiting the program.

## Requirements
Python 3.x

## How to Use
1. Run the script (python encryption.py).
2. Choose an option from the menu:
   - Encrypt a message
   - Decrypt a message
   - Exit

If you choose to encrypt a message, you will be prompted to enter the message, and the script will display the original and encrypted messages. If you choose to decrypt a message, you will be prompted to enter the encrypted message, and the script will display the decrypted message.

## Code Explanation

The script consists of the following main components:

- `generate_key()`: Generates a key for encryption and decryption.
- `encrypt_message(chars, keys, message)`: Encrypts a message using the generated key.
- `decrypt_message(chars, keys, message)`: Decrypts a message using the generated key.
- `main()`: The main function that provides a menu for the user to interact with the encryption and decryption functions.

## Author
[Aditya]

Feel free to explore, modify, and use this code as needed. If you encounter any issues or have suggestions, please let me know.