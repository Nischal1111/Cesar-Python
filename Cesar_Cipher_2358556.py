import os
# importing os to check if the file exists or not#


def welcome():
    # Using this function to greet the user#
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    # Using the function to prompt user for mode, shift and the message.#
    while True:  # Using loop to continuosuly ask user if they input the wrong command
        mode = input('Would you like to encrypt (e) or decrypt (d): ').lower()
        if mode != 'e' and mode != 'd':
            print('Invalid command')
        else:
            break
    message = input("What message would you like to {} ?:".format(
        "encrypt" if mode == "e" else "decrypt")).upper()
    while True:  # Using loop to continuosuly ask user if they input the wrong command
        try:
            shift = int(input("What is the shift number: "))
            break
        except ValueError:
            print("Invalid Shift")
    return mode, message, shift


def encrypt(message, shift):
    # Using the function to encrypt the message by given shift number.#
    encrypt_result = ""
    for char in message.upper():
        if char.isalpha():
            encrypt_result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            encrypt_result += char
    return encrypt_result


def decrypt(message, shift):
    # Using the function to decrypt the message by given shift number.#
    decrypt_result = ''
    for char in message.upper():
        if char.isalpha():
            decrypt_result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypt_result += char
    return decrypt_result


def process_file(filename, mode, shift):
    # Using the function to encrypt or decrypt the code after reading from the file given as input by the user.#
    try:
        with open(filename, 'r') as input_file:
            msg = input_file.read()
        if mode == "e":
            encrypted_result = ""
            for char in msg.upper():
                if char.isalpha():
                    encrypted_result += chr(ord(char) + shift)
                else:
                    encrypted_result += char
            write_message(encrypted_result)
            print(encrypted_result)
        elif mode == "d":
            decrypted_result = ""
            for char in msg.upper():
                if char.isalpha():
                    decrypted_result += chr(ord(char) - shift)
                else:
                    decrypted_result += char
            write_message(decrypted_result)
            print(decrypted_result)
    except FileNotFoundError:  # Shows file not found if file does not exist instesd of crashing
        print("File not found:", filename)


def is_file(filename):
    # Using the function to check if the file exists or not.#
    return os.path.isfile(filename)


def write_message(msg):
    # Using the function to encrypt or decrypt the file given by user and print result to result.txt#
    with open("result.txt", 'w') as f:
        f.write(msg)


def message_or_file():
    # Using the function to ask user for mode of conversion and whether to take message from console or the file#
    while True:
        valid_mode = ["e", "d"]
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        while mode not in valid_mode:  # Checks the mode and loops if user inputs any other value than 'e' or 'd'#
            print("Invalid mode. Please try again.")
            mode = input(
                "Would you like to encrypt (e) or decrypt (d)? ").lower()
        while True:  # Ask for the reading mode and loops if user inputs any other value than 'f' or 'c'#
            reading_mode = input(
                "Would you like to read from a file (f) or the console (c)? ").lower()
            if reading_mode not in ('f', 'c'):
                print("Invalid reading mode.")
                reading_mode = input(
                    "Would you like to read from a file (f) or the console (c)? ").lower()
            break
        while True:  # Ask for the shift number and loops if user inputs wrong value type and breaks if digit is passed#
            try:
                shift = int(input("What is the shift number ?: "))
                break
            except ValueError:
                print("Invalid Shift")
        if reading_mode == 'c':  # Reads the message from the console and converts as the user asks#
            message = input("What message would you like to {} ?: ".format(
                'encrypt' if mode == 'e' else 'decrypt'))
            if mode == "e":
                encrypted = encrypt(message, shift).upper()
                print(encrypted)
            elif mode == "d":
                decrypt(message, shift)
                decripted = decrypt(message, shift).upper()
                print(decripted)
        elif reading_mode == 'f':  # Reads the message from the file and converts as the user asks#
            while True:
                filename = input('Enter file:')
                if not is_file(filename):
                    print("File not found:", filename)
                    continue
                else:
                    process_file(filename, mode, shift)
                    print('Result printed to result.txt')
                break
            break
        break  # Breaks after the message is converted and printed in the console#


def main():
    # using the function to call the other funtions and asking again if the user wants to continue to convert the data.#
    welcome()
    while True:  # Starting the loop of converting the data#
        message_or_file()
        another_message = input(
            "Would you like to encrypt or decrypt another message? (y/n): ").upper()
        if another_message not in ("N", 'Y'):
            print('Invalid Command.')
            another_message = input(
                "Would you like to encrypt or decrypt another message? (y/n): ").upper()
        if another_message == 'N':
            print('Thank you for using the program, Goodbye!!!')
            break  # Breaking the loop user chooses to quit#


main()  # calling the function to run the overall program
