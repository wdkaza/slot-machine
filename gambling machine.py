import random
starting_balance = 1000
bet = 0
current_balance = starting_balance
play_again = True
choices = ["yes","no"]
def spinrow():
    symbols = ["🤑","😎","😡","🌟","🥶"]
    current_balance = starting_balance - bet
    return[random.choice(symbols) for i in range(3)]

def checkwinner():
    current_balance = starting_balance - bet
    if spin[0] == spin[1] ==spin[2]:
        if spin[0] == '🤑':
            return current_balance * 100
            print("YOU WON!!!")
        if spin[0] == '😎':
            return current_balance * 10
            print("YOU WON!!!")
        if spin[0] == '😡':
            return current_balance * 0.5
            print("YOU LOST!!!")
        if spin[0] == '🌟':
            return current_balance * 50
            print("YOU WON!!!")
        if spin[0] == '🥶':
            return current_balance * 25
            print("YOU WON!!!")
def set_bet():
    bet = int(input("How much would you like to bet?$$$: "))
    return bet
def try_again():
    if current_balance <= 0:
        print("you lost everything you had😱")
        play_again = False
    else:
        play_again = input("again?🤑(next one might be the jackpot): ")
        if play_again == choices[0]:
            play_again = True
        if play_again == choices[1]:
            play_again = False

while play_again == True:
    set_bet()
    spin = spinrow()
    print(spin)
    print("money left: ",current_balance)
    checkwinner()
    try_again()