# A really great calculator.
# @author A really great student.
import sys

memory = 0


# implemented from FR1
def add(val):
    global memory
    memory = memory + val
    print('Result: %d' % memory)

def percent():
    global memory
    memory = memory / 100
    print('Result: %f' %memory)


def about():
    print("""A really great calculator.
Version 1.0.""")    


def quit_calculator():
    sys.exit()


def main():

    # add any new commands to the following list
    # command - the name of the command for the user to invoke
    # function - the reference to the function that will invoke the command
    # needs_argument - true if the function needs a number inputted from the user
    functions = [
        {'command': 'add', 'function': add, 'needs_argument': True},
        {'command': 'about', 'function': about, 'needs_argument': False},
        {'command': 'quit', 'function': quit_calculator, 'needs_argument': False},
        {'command': 'percent', 'function': percent, 'needs_argument': False}
    ]
    
    while True:
        
        # request a command from the user
        # we really should handle upper and lowercase commands here
        print('Enter a command\n>', end='')
        k = input()
        
        # loop through the command list and see if we have a match
        for f in functions:
            if k == f['command']:
                if f['needs_argument']:
                    print('Enter a value:\n>', end='')
                    v = input() # read from the command line
                    v = float(v) # convert to float. We really should do error checking here
                    f['function'](v)
                else:
                    f['function']()
        # really should handle if the user did not input a valid command


if __name__ == '__main__':
    
    main()