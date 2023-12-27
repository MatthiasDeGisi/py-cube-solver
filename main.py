import os
import time
from sty import fg
import classes.Cube as c

if __name__ == "__main__":
    os.system("cls")
    cube1 = c.Cube()

    # Define a dictionary for function mapping
    turn_functions = {
        "f": cube1.f_turn,
        "f'": cube1.f_turn_prime,
        "b": cube1.b_turn,
        "b'": cube1.b_turn_prime,
        "u": cube1.u_turn,
        "u'": cube1.u_turn_prime,
        "d": cube1.d_turn,
        "d'": cube1.d_turn_prime,
        "r": cube1.r_turn,
        "r'": cube1.r_turn_prime,
        "l": cube1.l_turn,
        "l'": cube1.l_turn_prime,
    }

    while True:
        print(cube1)
        user_input = input(fg.rs + "Enter a move (q to quit): ").lower()

        if user_input == "q":
            break

        if user_input.lower() == "h":
            print(
                "Clockwise:\nF = front\nB = back\nU = top\nD = bottom\nL = left\nR = right\nCounterclockwise:\nAppend ' to input."
            )
            input("Press any key to continue.")

        # Use dictionary.get() with a default value to handle unrecognized input
        turn_function = turn_functions.get(user_input, None)

        if turn_function:
            turn_function()
            
        else:
            print("Input not recognized.")

    # exit the program
    print("Exiting...")