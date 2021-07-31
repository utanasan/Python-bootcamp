"""Написать игру в "камень-ножницы-бумага" против компьютера.

Запустить игру в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага).
Сгенерировать случайный выбор компьютера. Вывести выбор компьютера.
Определить победителя, выведя соответствующую информацию. Спросить пользователя - хочет ли он повторить игру.
Если хочет - повторить, не хочет - выйти из цикла"""

import random

choice_list = ['R','S','P']
computer_wins = [('R','S'), ('R','P'), ('S','P')]
user_wins = [('P','R'), ('P','S'), ('S','R')]

while True:
    user_choice = input("Enter your choice: R - rock, S - scissors, P - paper\n")
    computer_choice = random.choice(choice_list)
    print(f"Computer have chosen {computer_choice}")
    if computer_choice==user_choice:
        print(f"Drawn!")
    elif (computer_choice,user_choice) in computer_wins :
        print(f"Computer wins!")
    else:
        print(f"User wins!")
    print("Do you wish to continue the game? Enter Y or N")
    if input() == 'Y':
        continue
    else:
        break


