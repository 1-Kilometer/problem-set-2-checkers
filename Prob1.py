#====================================================
# Filename: Prob1.py
# 
# Your name: Miles Fukuhara
# Who did you work with (if anyone)?: Nope
# Estimate for time spent (in hrs)?: 1
#====================================================

import karel

# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a function below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.

def create_checkerboard():
    """ Main function to create the checkerboard pattern. """
    # You need to add code here\
    while not_facing_north():
        crusin()
        if front_is_blocked():
            while not_facing_north():
                turn_left()
            if front_is_blocked():
                spin()
            else:
                check_board()
                turn_left()
                if front_is_clear():
                    crusin()
                else:
                    while not_facing_east():
                        turn_left()
        spin()
    


# Remember to define any more helper functions you want down here

def backup(): #This is less of a helper function and more of a "storage" for a previous iteration of my code before I mess with it
    while front_is_clear():
        while not_facing_north():
            crusin()
            if front_is_blocked():
                while not_facing_north():
                    turn_left()
                if front_is_blocked():
                    end()
                check_board()
                turn_left()
                if front_is_clear():
                    crusin()
                else:
                    while not_facing_east():
                        turn_left()
        spin()
    

def spin():
    for i in range(4):
        turn_left()

def check_board():
    if beepers_present():
        move()
    else:
        move()
        put_beeper()

def crusin():
    while front_is_clear():
        check_board()
