import random
from art import logo


# creating the function for getting a random card from the cards list
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# calculate_value() for checking wheather a user or computer had a black jack or not or if score is greater than 21 and had an ace with value 11 it will replace it with 1
def calculate_value(car_d):
    if sum(car_d) > 21 and len(car_d) == 2:
        return 0
    if 11 in car_d and sum(car_d) > 21:
        car_d.remove(11)
        car_d.append(1)
    return sum(car_d)


# compare () is for comparing both scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw !! ")
    elif user_score > 21:
        print("You Went Over !!")
        print("You Lose ")
    elif user_score > 21 and computer_score > 21:
        print("You Went Over !!")
        print("You Lose")
    elif computer_score > 21:
        print("You Win ")
        print("Computer Went Over ")
    elif computer_score == 0:
        print("You Lose , Computer Had a blackJack !!")
    elif user_score == 0:
        print("You Win , Victory With a BlackJack!!!")
    elif computer_score > user_score:
        print("You Lose")
    else:
        print("You Win")


# Play_game() is for playing the game with it's rules
def Play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        is_play_game = False
    while not is_play_game:
        user_score = calculate_value(user_cards)
        computer_score = calculate_value(computer_cards)
        print(f" Your cards are {user_cards} And Your Score is {user_score}")
        print(f" Computer First Card is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_play_game = True
        else:
            user_should_deal = input("Type y to draw a card or type n to go ahead ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_play_game = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_value(computer_cards)
    print(f" Your Final Hand {user_cards} , And Your final Score {user_score}")
    print(f" Computer Final Hand {computer_cards} , Computer Final Score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    Play_game()
