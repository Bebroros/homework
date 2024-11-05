from pathlib import Path


def opening_file(filepath, mode):
    try:
        with open(filepath, mode=f'r{mode}') as file:
            amount_of_lines = sum(1 for line in file)
        return amount_of_lines
    except UnicodeDecodeError:
        return "File cannot be opened"


def ask_directory():
    while True:
        try:
            filepath = Path(input("Input path to your file: "))
            if filepath.is_file() and filepath.exists():
                break
            else:
                print("This is not a file or file does not exist, try again")
        except ValueError:
            print("Please enter a valid path")
    return filepath


def ask_type_of_opening():
    while True:
        action = input('Do you want to open a file in text or binary mode?').lower()
        if action.startswith('t'):
            return 't'
        elif action.startswith('b'):
            return 'b'
        else:
            print("Please enter either 't' or 'b'")


def main():
    while True:
        filepath = ask_directory()
        print("File is found!")
        mode = ask_type_of_opening()
        print(f'Opening file in {'binary' if mode == 'b' else 'text'} format')
        print(opening_file(filepath, mode))
        if input('Do you want to continue?').lower().startswith('n'):
            break


if __name__ == '__main__':
    main()
