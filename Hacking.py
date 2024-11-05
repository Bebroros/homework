import random
import nltk
from nltk.corpus import words


def generate_random_words():
    nltk.download('words')
    list_of_words = [word for word in words.words() if len(word) == 7]
    punctuation = list(r'!"#$%&()*+,-./:;<=>?@][\^_`{|}~')
    list_of_password = [random.choice(list_of_words).upper() for _ in range(1, 11)]
    list_of_random_words = [(f'0x1{random.randint(1, 2)}{random.randint(1, 9)}0'
                             f'{''.join([random.choice(punctuation) for _ in range(0, random.randint(1, 5))])}'
                             f'{list_of_password[x-1]}'
                             f'{''.join([random.choice(punctuation) for _ in range(0, random.randint(1, 5))])}')
                            for x in range(1, 11)]
    list_of_random_words += [(f'0x1{random.randint(1, 2)}{random.randint(1, 9)}0'
                             f'{''.join([random.choice(punctuation) for _ in range(0, random.randint(10, 15))])}')
                             for _ in range(0, 3)]
    random.shuffle(list_of_random_words)
    return list_of_random_words, list_of_password


def main():
    while True:
        list_of_random_words, list_of_passwords = generate_random_words()
        for word in list_of_random_words:
            print(word)
        password = random.choice(list_of_passwords)
        for x in range(4, -1, -1):
            if x == 0:
                print('Access Denied')
                print('Password was:', password)
                break
            guess = input(f'Enter password: ({x} tries remaining)')
            if guess.upper() == password:
                print('A C C E S S G R A N T E D')
                break
            else:
                similarity_count = 0
                bebra = list(set(list(guess.upper())))
                for letter in list(set(list(guess.upper()))):
                    if letter in password:
                        similarity_count += 1
                print(f"Access Denied({similarity_count}/7 correct)")
        if input('Type (N) if you want to quit').upper() == 'N':
            break


if __name__ == '__main__':
    main()
