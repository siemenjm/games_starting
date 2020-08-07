import random

money = 100

#Write your game of chance functions here

# Heads or tails.
def coin_flip(bet, choice):
    print("We're flipping a coin! Heads or tails?")
    print("You bet $" + str(bet) + " on " + choice + ".")
    if choice == "Heads":
        num_choice = 0
    elif choice == "Tails":
        num_choice = 1
    lands_up = random.randint(0,1)
    if lands_up == num_choice:
        print(choice + "! You win $" + str(bet) + "!")
        return bet
    else:
        if lands_up == 0:
            actual = "Heads"
        elif lands_up == 1:
            actual = "Tails"
        print(actual + "! You lose $" + str(bet) + "...")
        return bet*(-1)

# Cho-Han.
def cho_han(bet, choice):
    print("We're playing Cho-han! Odd or even?")
    print("You bet $" + str(bet) + " on " + choice + ".")
    if choice == "Odd":
        remainder = 1
    elif choice == "Even":
        remainder = 0
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    sum = die1 + die2
    if sum % 2 == remainder:
        print(choice + "! You win $" + str(bet) + "!")
        return bet
    else:
        if sum % 2 == 0:
            actual = "Even"
        elif sum % 2 == 1:
            actual = "Odd"
        print(actual + "! You lose $" + str(bet) + "...")
        return bet*(-1)

# High card wins.
def high_card(bet):
    print("High card wins!")
    print("You bet $" + str(bet) + " that you will draw a higher card than your opponent.")

    # Build deck with associated numerical values.
    card_values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
    suit_names = {0: "Spades", 1: "Clubs", 2: "Hearts", 3: "Diamonds"}
    total_deck = {0:card_values, 1:card_values, 2:card_values, 3:card_values}

    # Draw cards.
    my_suit = random.randint(0, 3)
    my_card = random.randint(2, 14)
    opponent_suit = random.randint(0, 3)
    opponent_card = random.randint(2, 14)
    # Makes sure opponent can't draw same card as me.
    while my_suit == opponent_suit and my_card == opponent_card:
        opponent_card = random.randint(2, 14)
    print("You drew the " + str(card_values.get(my_card)) + " of " + suit_names.get(my_suit) + ".")
    print("Your oppenent drew the " + str(card_values.get(opponent_card)) + " of " + suit_names.get(opponent_suit) + ".")

    # Compare card values.
    if my_card == opponent_card:
        print("It's a tie! Double or nothing! The deck will be reshuffled.")
        bet = high_card(bet*2)
        return bet
    elif my_card > opponent_card:
        print("You drew the higher card! You win $" + str(bet) + "!")
        return bet
    else:
        print("Your opponent drew the higher card... You lose $" + str(bet) + "...")
        return bet*(-1)

# Roulette.
def roulette(bet, choice):
    print("We're playing roulette! Where will the ball land?")
    if choice == "Odd" or choice == "Even":
        print("You bet $" + str(bet) + " that the ball will land on an " + choice.lower() + " number.")
    elif choice == "00":
        print("You bet $" + str(bet) + " that the ball will land on " + choice + ".")
    else:
        print("You bet $" + str(bet) + " that the ball will land on " + str(choice) + ".")

    # Roulette wheel.
    wheel = [*range(37)]
    wheel.append("00")
    landed_on_index = random.randint(0,37)
    landed_on = wheel[landed_on_index]

    if landed_on == "00" and choice == "00":
        winnings = bet * 35
        print("The ball landed on 00! You win $" + str(winnings) + "!")
        return winnings
    elif landed_on == 0 and choice == 0:
        winnings = bet * 35
        print("The ball landed on 0! You win $" + str(winnings) + "!")
        return winnings
    elif choice == "Odd":
        if landed_on_index % 2 == 1:
            print("The ball landed on " + str(landed_on) + "! You win $" + str(bet) + "!")
            return bet
        else:
            print("The ball landed on " + str(landed_on) + "... You lose $" + str(bet) + "...")
            return bet * (-1)
    elif choice == "Even":
        if landed_on_index % 2 == 0 and landed_on != 0:
            print("The ball landed on " + str(landed_on) + "! You win $" + str(bet) + "!")
            return bet
        else:
            print("The ball landed on " + str(landed_on) + "... You lose $" + str(bet) + "...")
            return bet * (-1)
    elif landed_on == choice:
        winnings = bet * 35
        print("The ball landed on " + str(landed_on) + "! You win $" + str(winnings) + "!")
        return winnings
    else:
        print("The ball landed on " + str(landed_on) + "... You lose $" + str(bet) + "...")
        return bet * (-1)

# Checks to make sure a player can't bet more money than they have.
def money_check(bet)
    if bet > money:
        print("You can't bet more money than you have!!! Come back after visiting the ATM...")
        return False
    else:
        return True


#Call your game of chance functions here
money += coin_flip(10, "Heads")
print("You have $" + str(money) + " remaining.")
print()

money += cho_han(10, "Odd")
print("You have $" + str(money) + " remaining.")
print()

money += high_card(10)
print("You have $" + str(money) + " remaining.")
print()

money += roulette(10, "Even")
print("You have $" + str(money) + " remaining.")
print()