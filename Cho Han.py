import random


def calculating(choice, sum_of_rolls):
    if choice == 'Cho' and sum_of_rolls % 2 == 0:
        return True
    elif choice == 'Han' and sum_of_rolls % 2 == 0:
        return False
    elif choice == 'Han' and sum_of_rolls % 2 != 0:
        return True
    elif choice == 'Cho' and sum_of_rolls % 2 != 0:
        return False


def users_guess():
    while True:
        guess = input('Cho or Han?(even or odd)').lower()
        if guess == 'cho':
            return 'Cho'
        elif guess == 'han':
            return 'Han'
        else:
            print("Please enter either 'Cho' or 'Han'")


def generating_rolls():
    JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}
    first_roll = random.randint(1, 6)
    second_roll = random.randint(1, 6)
    sum_of_rolls = first_roll + second_roll
    return sum_of_rolls, JAPANESE_NUMBERS[first_roll], JAPANESE_NUMBERS[second_roll]


def making_bet(money):
    while True:
        print(f'You have {money} money')
        action = input('Do you want to make a bet?(Y/N)')
        if action.upper() == 'Y':
            while True:
                try:
                    bet = int(input('How much money would you like to bet?'))
                    if bet > money:
                        print('Bet is more than amount of money.')
                    else:
                        money -= bet
                        return money, bet
                except ValueError:
                    print('Please enter a valid number.')
        if action.upper() == 'N':
            input('Press Enter to continue...')
            quit()
        else:
            print('Please enter a YES or NO.')


def main():
    money = 5000
    while money > 0:
        money, bet = making_bet(money)
        print(f"You made a bet of {bet} money. You have {money} money left")
        print('Throwing two dices...')
        choice = users_guess()
        print(f'Your guess is {choice}')
        input('Press Enter to continue...')
        sum_of_rolls, first_roll, second_roll = generating_rolls()
        print(f'The first number is {first_roll}, the second number is {second_roll}.'
              f'\nIt`s {sum_of_rolls}.')
        if calculating(choice, sum_of_rolls):
            print('You win!')
            money += (2*bet-40)
        else:
            print('You lose!')
    else:
        print('You`ve got no money left!')
        input('Press Enter to Exit.')


if __name__ == '__main__':
    main()
