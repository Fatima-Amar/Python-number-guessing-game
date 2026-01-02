# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 22:05:06 2025

@author: Fatyma Amar
"""
play_again = "yes" #It creates a variable named play_again and stores the word "yes" inside it.


# input() lets the user type something in the terminal
name = input("Enter your name: ")

# We join text + the name using +
print("Welcome,", name + "! Let's play the Number Guessing Game.")



#python number guessing game
import random #needs Python’s random module to generate a random number for the player to guess
#to ask user opinion on if they want to countinou with game or not
#indenting the while loop so it runs under the while loop of yes and no question
while play_again.lower() in ("yes", "y"):
#while loop asking yes or not/ all the value will be indented in this while loop
# now we assign variable for lowest and highest no
    lowest_num = 1
    highest_num = 20
    # RANDINT is a function in Python that picks a random integer between two numbers you give it.
    answer = random.randint(lowest_num, highest_num)
    
    #we want user to keep guessing and application to keep running. # we use variable
    guesses = 0
    # a bolean variable for is running, so the application keeps running.
    is_running = True
    
    
    #now we will prompt the user using the f string 
    print(f"Select a number between {lowest_num} and {highest_num}")
    # we will add two place holders in {} brackets to select no
    
    # we will need while loop to countinue the game in each round
    while is_running:
        guess = input("Enter your guess")
        #we put isdigit function to let user know that they are allowed to put only digit no not words such as pizza.
        if guess.isdigit():
            guess = int(guess) #we will reassign our guess as as an integer becuase before its a string
            guesses += 1 #limit no of guesses to 1 #+= is called an augmented assignment operator.
            
            if guess < lowest_num or guess > highest_num: #if the user put no out of range
                print("That number is out of range")
                print(f"Please select a number between {lowest_num} and {highest_num}")
            elif guess < answer: #if guess  is less than the answer
                print("📉 Too low! Try again!") 
            elif guess > answer: #if guess is greater than the answer
                print("📈 Too high! Try again!")
            else:
                print(f"🎉Correct! The answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False
                
        
        else:
            print("Invalid guess")
            print(f"Please select a number between {lowest_num} and {highest_num}")
    play_again = input("Do you want to play again? (yes/no): ")
    #while loop to ask if game should countinou or not
           
 
print("Thank you for playing", name + "!")
print("Hope you enjoyed the game! 😊")
print("See you soon!🫶🏼")


