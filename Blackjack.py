import random
import Art
import os
import math


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.


def DealCards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def CalculateScores(Cards):
    if sum(Cards) == 21 and len(Cards) == 2:
        return 0
    if 11 in Cards and sum(Cards) > 21:
        Cards.remove(11)
        Cards.append(1)
    return sum(Cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    Art.bank += math.ceil(Art.bet / 2)
    print(Art.bank)
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    Art.bank += ceil(Art.bet * 2.5)
    print(Art.bank)
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    Art.bank += Art.bet * 2
    print(Art.bank)
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    Art.bank += Art.bet * 2
    print(Art.bank)
    return "You win 😃"
  else:
    return "You lose 😤"

def PlayGame():
    print(Art.logo)
    print(f"Your bank is {Art.bank}")
    Art.bet = int(input(f"How much would you like to bet from 1 to {Art.bank}? "))
    UserCards = []
    ComputerCards = []
    isGameOver = False
    Art.bank -= Art.bet
    print(Art.bank)
    for c in range(2):
        UserCards.append(DealCards())
        ComputerCards.append(DealCards())
    while not isGameOver:
        UserScore = CalculateScores(UserCards)
        ComputerScore = CalculateScores(ComputerCards)
        print(f"   Your cards: {UserCards}, current score: {UserScore}")
        print(f"   Computer's first card: {ComputerCards[0]}")
        if UserScore == 0 or ComputerScore == 0 or UserScore > 21:
            isGameOver = True
        else:
            Hit = input("Would you like another card? 'y' or 'n' : ")
            if Hit == "y":
                UserCards.append(DealCards())
            else:
                isGameOver = True
    while ComputerScore != 0 and ComputerScore < 17:
        ComputerCards.append(DealCards())
        ComputerScore = CalculateScores(ComputerCards)

    print(f"   Your final hand: {UserCards}, final score: {UserScore}")
    print(f"   Computer's final hand: {ComputerScore}, final score: {ComputerScore}")
    print(compare(UserScore, ComputerScore))


while input("Would you like to place a bet? 'y' or 'n' ") == "y":
    clear = lambda: os.system('cls')
    clear()
    PlayGame()
