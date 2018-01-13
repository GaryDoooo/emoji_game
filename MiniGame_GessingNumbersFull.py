# line1= '______________________'
# line2= ' 1 2 3 4 5 6 7 8 9 10 '
# line3= ' | | | | | | | | | | | '
# line4= ' |                   | '
# line5= ' |___________________| '

from terminaltables import SingleTable
import subprocess as sp
from numpy import random

#print ('jadfksjkladfsjdfs')

def print_table(guessed_result):
    newlist=[[1,2,3,4,5,6,7,8,9,10],guessed_result]
    table=SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border=False
    table.title="Number List"
    # sp.call("clear",shell=True)
    print(table.table)

def guess_a_number():
    print ('HOW TO PLAY | GUESSING NUMBERS:')
    print (' - GUESS THE NUMBER')
    print (' - S = SMALL')
    print (' - L = LARGE')
    guessed_result=[""]*10
    number=random.randint(1,high=11)
    for _ in range(3):
        print_table(guessed_result)
        try:
            guess=int(input("Please Input Your Guess: "))
            if guess<1 or guess >10:
                print("Lose one round. Please input an integer from 1 to 10.")
            elif guess < number:
                print("Your guess is small.")
                guessed_result[guess-1]="S"
            elif guess > number:
                print ('Try Agian(your guess is too large)')
                guessed_result[guess-1]="L"
            else:
                print("You got it!")
                return True
        except ValueError:
            print("Lose one round. Please input an integer from 1 to 10.")
        
    return False
        
    

def main():
    if guess_a_number():
        print("You win.")
    else:
        print("You loss.")

if __name__ == "__main__":
    main()    
