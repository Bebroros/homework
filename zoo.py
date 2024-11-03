class Animal:
    def __init__(self, name, worker_of_zoo):
        self.name = name
        if worker_of_zoo.feeding[self.name.split()[-1]]:
            self.hunger = False
        else:
            self.hunger = True
        if self.hunger or not worker_of_zoo.cleaning:
            self.happiness = False
        else:
            self.happiness = True


class Worker:
    def __init__(self, cleaning, feeding, opened):
        self.cleaning = cleaning
        self.feeding = feeding
        self.opened = opened


class Aviary:
    def __init__(self, worker):
        if worker.cleaning:
            self.Aviary_cleaned = True
        else:
            self.Aviary_cleaned = False
        if worker.opened:
            self.Aviary_opened = True
        else:
            self.Aviary_opened = False


def annas_action():
    feedings_of_animal = {}
    opened = input("Has Anna opened the aviary?(Y/N):")
    if opened.upper() == "Y":
        opened = True
        print("Today Anna opened the aviary...")
    elif opened.upper() == "N":
        opened = False
        print("Today Anna forgot to open the aviary...")
    else:
        print('Invalid input, try again')
        return annas_action()
    cleaning = input("Has Anna cleaned the aviary?(Y/N):")
    if cleaning.upper() == "Y":
        cleaning = True
        print("Today Anna cleaned the aviary...")
    elif cleaning.upper() == "N":
        cleaning = False
        print("Today Anna forgot to clean the aviary...")
    else:
        print('Invalid input, try again')
        return annas_action()
    feeding = input("Has Anna fed the pig?(Y/N):")
    if feeding.upper() == "Y":
        print("Today Anna fed the pig...")
        feedings_of_animal['pig'] = True
    elif feeding.upper() == "N":
        feedings_of_animal['pig'] = False
        print("Today Anna forgot to feed the pig...")
    feeding = input("Has Anna fed the rabbit?(Y/N):")
    if feeding.upper() == "Y":
        print("Today Anna fed the rabbit...")
        feedings_of_animal['rabbit'] = True
    elif feeding.upper() == "N":
        feedings_of_animal['rabbit'] = False
        print("Today Anna forgot to feed the rabbit...")
    feeding = input("Has Anna fed the goat?(Y/N):")
    if feeding.upper() == "Y":
        print("Today Anna fed the goat...")
        feedings_of_animal['goat'] = True
    elif feeding.upper() == "N":
        print("Today Anna forgot to feed the goat...")
        feedings_of_animal['goat'] = False
    else:
        return annas_action()
    return Worker(cleaning, feedings_of_animal, opened)


def main():
    Anna = annas_action()
    barn = Aviary(Anna)
    pig = Animal('Georg the pig', Anna)
    rabbit = Animal('Peter the rabbit', Anna)
    goat = Animal('Fred the goat', Anna)
    for animal in pig, rabbit, goat:
        print(f'{animal.name} is {'happy' if animal.happiness else "not happy"}'
              f'{", because of hunger" if animal.hunger and not animal.happiness else ''} '
              f'{", because of dirty enclosure" if not barn.Aviary_cleaned and not animal.happiness else ''}', sep='')
    print("Animals went out of enclosure and walked around" if barn.Aviary_opened
          else 'Animals stayed at their enclosure, because it was not open')


if __name__ == '__main__':
    main()
