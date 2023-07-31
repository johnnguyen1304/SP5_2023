import random

# Function to get user's choice
def getUserChoice():
    user = int(input('Rock(1), Paper(2) or Scissors(3)? '))
    while user < 1 or user > 3:
        print('Invalid input - please enter the number 1, 2 or 3.')
        user = int(input('Rock(1), Paper(2) or Scissors(3)? '))
    return user

# Function to ask if play again
def askPlayAgain():
    ans = ""
    while ans not in ['Y', 'y', 'N', 'n']:
        ans = input('Play again (y|n)? ')
    return ans

# Function to play the game
def playGame():
    play = 'y'
    noGames = 0
    selection = ['Rock', 'Paper', 'Scissors']
    role = ['crushes', 'covers', 'cut']

    # Number codes for rock, paper, scissors
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    # build list of all winning combinations
    winningCombos = [[PAPER, ROCK], [SCISSORS, PAPER], [ROCK, SCISSORS]]

    # Repeat while the user wants to play
    while play in ['y', 'Y']:
        # Prompt for and read user's choice
        user = getUserChoice()
        # Display user's choice as text to the screen
        print('You chose', selection[user - 1])

        # Randomly generate computer's choice
        comp = random.randint(1, 3)
        # Display computer's "choice" as text to the screen
        print('Computer chose', selection[comp - 1])

        # Find a winner.
        # build current combination
        currentCombo = [user, comp]
        if comp == user:
            print('Draw - no winner!')
        elif any(currentCombo == combo for combo in winningCombos):
            print('You win -', selection[user - 1], role[user - 1], selection[comp - 1])
        else:
            print('You lose -', selection[comp - 1], role[comp - 1], selection[user - 1])

        noGames = noGames + 1
        play = askPlayAgain()
        print()

    # Show final results
    if noGames == 1:
        print("You played", noGames, "game!")
    else:
        print("You played", noGames, "games!")
    print('Thanks for playing!')


# Main entry of the program
playGame()
