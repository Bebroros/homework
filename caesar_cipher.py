from cryptography.fernet import Fernet
import rsa


"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher"""

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        # Your code goes here
        encrypted_message = []
        for symbol in message:
            if symbol in SYMBOLS:
                new_index = SYMBOLS.index(symbol) - self.key
                encrypted_message += [SYMBOLS[new_index]]
            else:
                encrypted_message += [symbol]
        return f"Your message is '{''.join(encrypted_message)}'."

    def decrypt(self, message):
        # Your code goes here
        decrypted_message = []
        for symbol in message:
            if symbol in SYMBOLS:
                new_index = SYMBOLS.index(symbol) + self.key
                if new_index >= len(SYMBOLS):
                    new_index -= len(SYMBOLS)
                decrypted_message += [SYMBOLS[new_index]]
            else:
                decrypted_message += [symbol]
        return f"You message is {'' .join(decrypted_message)}."


def get_user_mode():
    while True:  # Keep asking until the user enters e or d.
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()

        if response.startswith("e"):
            return "encrypt"
        elif response.startswith("d"):
            return "decrypt"
        else:
            print("Please enter the letter 'e' or 'd'.")


def get_user_key():
    while True:  # Keep asking until the user enters a valid key.
        max_key = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ")

        if not response.isdecimal():
            continue

        response = int(response)

        if 0 <= response <= max_key:
            return response


def get_algorithm():
    algorithm = input("Please enter the algorithm you want to use(Caesar, Fernet, RSA): ").lower()
    if algorithm.startswith('c'):
        return 'caesar'
    elif algorithm.startswith('f'):
        return 'fernet'
    elif algorithm.startswith('r'):
        return 'rsa'
    else:
        print("Please enter the letter 'c' or 'f' or 'r'.")
        return get_algorithm()


def fernet_encrypt(message):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    print("Here is encrypted message")
    print(str(fernet.encrypt(message)).strip('b"'))
    print('Here is your key')
    print(str(key).strip('b"'))


def fernet_decrypt(message):
    key = input('enter a key')
    fernet = Fernet(key)
    print("Here is decrypted message")
    print(str(fernet.decrypt(message)).strip('b"'))


def generate_keys_rsa():
    (pubkey, privkey) = rsa.newkeys(2048)
    with open('public.pem', 'wb') as file:
        file.write(pubkey.save_pkcs1('PEM'))
    with open('private.pem', 'wb') as file:
        file.write(privkey.save_pkcs1('PEM'))
    return pubkey, privkey


def load_keys_rsa():
    with open('public.pem', 'rb') as file:
        pubkey = rsa.PublicKey.load_pkcs1(file.read())
    with open('private.pem', 'rb') as file:
        privkey = rsa.PrivateKey.load_pkcs1(file.read())
    return pubkey, privkey


def encrypt_message_rsa(message, pubkey):
    return rsa.encrypt(message.encode(), pubkey)


def decrypt_message_rsa(message, privkey):
    return rsa.decrypt(eval(message), privkey).decode()


def main():
    algorithm = get_algorithm()
    if algorithm == 'caesar':
        mode = get_user_mode()  # Let the user enter if they are encrypting or decrypting
        key = get_user_key()  # Let the user enter the key to use

        coder = CaesarCipher(key)

        # Let the user enter the message to encrypt/decrypt
        print(f"Enter the message to {mode}.")
        message = input("> ").upper()  # Caesar cipher only works on uppercase letters

        if mode == "encrypt":
            # Stores the encrypted/decrypted form of the message
            translated = coder.encrypt(message)
        else:
            translated = coder.decrypt(message)

        # Display the encrypted/decrypted string to the screen
        print(translated)
    elif algorithm == 'fernet':
        mode = get_user_mode()
        message = input(f'Enter the message to {mode}.').encode()
        if mode == 'encrypt':
            fernet_encrypt(message)
        elif mode == 'decrypt':
            fernet_decrypt(message)
    elif algorithm == 'rsa':
        mode = get_user_mode()
        message = input(f'Enter the message to {mode}.')
        try:
            pubkey, privkey = load_keys_rsa()
        except FileNotFoundError:
            pubkey, privkey = generate_keys_rsa()
        if mode == 'encrypt':
            print(encrypt_message_rsa(message, pubkey))
        elif mode == 'decrypt':
            print(decrypt_message_rsa(message, privkey))
        else:
            print('Invalid input')


if __name__ == "__main__":
    print("Caesar Cipher")
    print("The algorithm encrypts letters by shifting them over by a")
    print("key number. For example, a key of 2 means the letter A is")
    print("encrypted into C, the letter B encrypted into D, and so on.")
    print()

    while True:
        main()

        print("\n\nDo you want to run cipher one more time? Y or N")
        repeat = input("> ").lower()

        if repeat != "y":
            print("Thank you!")
            break
