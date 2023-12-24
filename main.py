import os
import time
from sty import fg
import classes.Cube as c

os.system("cls")
cube1 = c.Cube()
while True:
    print(f"\n{cube1}")
    user_input = input(fg.rs + "Turn (h for help): ")
    if user_input.lower() == "h":
        print(
            "Clockwise:\nF = front\nB = back\nT = top\nD = bottom\nL = left\nR = right\nCounterclockwise:\nAppend ' to input."
        )
        input("Press any key to continue.")
        
    elif user_input.lower() == "f":
        cube1.f_turn()
        
    elif user_input.lower() == "f'":
        cube1.f_turn_prime()
        
    elif user_input.lower() == "b":
        cube1.b_turn()
        
    elif user_input.lower() == "b'":
        cube1.b_turn_prime()
        
    else:
        print("Input not recognized.")
