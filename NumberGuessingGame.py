#PYTHON CODE FOR THE NUMBER GUESSING GAME"

import random

print("Hi! Welcome to Guess the number game!")
level = input("Choose your difficulty level: Easy, Medium or Hard")
if level == "Easy":
    chances = 10
if level == "Medium":
    chances = 7
if level == "Hard":
    chances = 5
print("You chose ",level," Guess a number between 0 to 100. You'll have to guess the number in ",chances," chances!")
number = int(random.random()*100)
guesses = 0
while guesses < chances:
    user_guess = int(input("Enter your guess:"))
    guesses+=1

    if number == user_guess:
        print("Congratulations genius! The number is ",number,", and you have guessed it in ",guesses," guess!")
        break
    elif chances - guesses == 0:
        print("Sorry the number is ",number," Game Over! But Better luck next time!")
        break
    elif number > user_guess:
        print("Oops! you guessed too low! Better luck next time. You have only",chances - guesses, "guesses left!")
    elif number < user_guess:
        print("Oops! you guessed too high! Better luck next time. You have only",chances - guesses, "guesses left!")

