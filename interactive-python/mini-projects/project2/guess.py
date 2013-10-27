# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import math
import random
import simplegui

# Set seed for testing purposes to reproduce the random sequence
#random.seed = 0


#def number_of_guesses(low,high):
#    return int(math.ceil(math.log(high - low + 1) /math.log(2)))

# initialize global variables used in your code

# Store randomly generated "secret" number
secret_number = 0

# Tracks the number of guesses made by the player
guess_count = 0

# Set defaults for range and number of guesses
num_range = 100
guesses_left = 7


# helper function to start and restart the game
def new_game():
    """
    (None) -> None
    
    Initializes a new game.
    """
    global num_range,secret_number,guesses_left
  
    # Generate a new random number in the specified range
    secret_number = random.randrange(0,num_range+1)
    
    # Compute the number of allowed guesses based on the range
    guesses_left = int(math.ceil(math.log(num_range + 1) /math.log(2)))

    # Inform the player that it is a new game, the range and number of guesses.
    print("\nNew game. Range is from 0 and " + str(num_range))
    print("Number of remaining guesses is " + str(guesses_left))


# define event handlers for control panel
def range100():
    """ (None) -> None
    
    Sets the range of the random number generation from 0 to 100
    and restarts the game when the button associated with this
    handler is depressed
    """
    global num_range
    
    # button that changes range to range [0,100) and restarts
    num_range = 100
    
    # Restart game
    new_game()
    
def range1000():
    """ (None) -> None
    
    Sets the range of the random number generation from 0 to 1000
    and restarts the game when the button associated with this
    handler is depressed
    """
    global num_range

    # button that changes range to range [0,1000) and restarts
    num_range = 1000

    new_game()
        
    
def input_guess(guess):
    """
    (str) -> None
    
    Handler when the player guesses a value. guess is a string from the input field.
    """
    global secret_number, guesses_left
    
    # Convert string to a number
    number = int(guess)
    print("\nGuess was " + str(number))

    # Increment our counter which tracks the number of guess attempts
    guesses_left = guesses_left - 1

    # Inform the player the number of guesses they have left.
    print("Number of remaining guesses is " + str(guesses_left))
    
    # Check for a match or provide feedback to player
    if (number == secret_number):
        print("Correct!")
        new_game()
    elif (guesses_left == 0):
        print("You ran out of guesses. The number was " + str(secret_number))
        new_game()
    elif (number > secret_number):
        print("Lower!")
    else:
        print("Higher!")
    


f = simplegui.create_frame('Guess the number',200,200)

# register event handlers for control elements
f.add_button('Range: 0 - 100',range100,200)
f.add_button('Range: 0 - 1000',range1000,200)
f.add_input('Enter a guess',input_guess,200)



# call new_game and start frame
new_game()
f.start()


# always remember to check your completed program against the grading rubric
