"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    pass
    while facing_east():
        if front_is_clear():
            move()
        else:
            pass
        jump()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    up()
    cross()
    down()


def up():
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()
    turn_left()
    while not right_is_clear():
        move()

def cross():
    # while not facing_east():
    #     turn_right()
    # move()
    # while not facing_south():
    #     turn_right()
    turn_right()
    move()
    turn_right()


def down():
   while facing_south():
       if front_is_clear():
           move()
       else:
           turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
