"""Cube class.
"""
from sty import fg


class Cube:
    def __init__(self):
        """Construct a solved cube."""
        # mapping side icons to colours for printing
        G = fg(0, 255, 0) + "G"
        B = fg(0, 0, 255) + "B"
        W = fg(255, 255, 255) + "W"
        Y = fg(255, 234, 0) + "Y"
        R = fg(255, 0, 0) + "R"
        O = fg(255, 165, 0) + "O"
        # Next 6 attributes are the sides
        self.__front = [[R, G, G], [B, G, G], [Y, G, G]]
        self.__back = [[B, B, B], [B, B, B], [B, B, B]]
        self.__top = [[W, W, W], [W, W, W], [W, W, W]]
        self.__bottom = [[Y, Y, Y], [Y, Y, Y], [Y, Y, Y]]
        self.__right = [[R, R, R], [R, R, R], [R, R, R]]
        self.__left = [[O, O, O], [O, O, O], [O, O, O]]
        # side mapping for getters and setters
        self.side_mapping = {
            "front": self.__front,
            "back": self.__back,
            "top": self.__top,
            "bottom": self.__bottom,
            "right": self.__right,
            "left": self.__left,
        }

    def get_side(self, side: str) -> list:
        """Return the array representation of a side.

        Args:
            side (str): the side to return

        Returns:
            list: the representation of the side
        """
        return self.side_mapping[side]

    def f_turn(self) -> None:
        """Turn the front side of the cube clockwise.
        This works by saving the state of all the relevant sides,
        then reassigning items in the array by referencing parts of the original.
        """

        # Save the original states for reference
        original_front = [row[:] for row in self.__front]
        original_top = [row[:] for row in self.__top]
        original_right = [row[:] for row in self.__right]
        original_bottom = [row[:] for row in self.__bottom]
        original_left = [row[:] for row in self.__left]

        # Turn front side
        for i in range(3):
            for j in range(3):
                self.__front[j][2 - i] = original_front[i][j]

        # Update top side
        for i in range(3):
            self.__top[2][i] = original_left[2 - i][2]

        # Update right side
        for i in range(3):
            self.__right[i][0] = original_top[2][i]

        # Update bottom side
        for i in range(3):
            self.__bottom[0][i] = original_right[i][0]

        # Update left side
        for i in range(3):
            self.__left[i][2] = original_bottom[0][i]

    def f_turn_prime(self) -> None:
        """Turn the front side of the cube counter-clockwise.
        This works by turning clockwise 3 times.
        """
        for i in range(3):
            self.f_turn()

    def b_turn(self) -> None:
        """Turn the back side of the cube clockwise.
        This works by saving the state of all the relevant sides,
        then reassigning items in the array by referencing parts of the original.
        """
        # Save the original states for reference
        original_back = [row[:] for row in self.__back]
        original_top = [row[:] for row in self.__top]
        original_left = [row[:] for row in self.__left]
        original_bottom = [row[:] for row in self.__bottom]
        original_right = [row[:] for row in self.__right]

        # turn the back side
        for i in range(3):
            for j in range(3):
                self.__back[j][2 - i] = original_back[i][j]

        # update the top side
        for i in range(3):
            self.__top[0][i] = original_right[i][2]

        # update the left side
        for i in range(3):
            self.__left[i][0] = original_top[0][2 - i]

        # update the bottom side
        for i in range(3):
            self.__bottom[2][i] = original_left[i][0]

        # update the right side
        for i in range(3):
            self.__right[i][2] = original_bottom[2][2 - i]

    def b_turn_prime(self) -> None:
        """Turn the back side of the cube counter-clockwise.
        This works by turning clockwise 3 times.
        """
        for i in range(3):
            self.b_turn()

    def u_turn(self) -> None:
        """Turn the top side of the cube clockwise.
        This works by saving the state of all the relevant sides,
        then reassigning items in the array by referencing parts of the original.
        """
        # Save the original states for reference
        original_top = [row[:] for row in self.__top]
        original_front = [row[:] for row in self.__front]
        original_right = [row[:] for row in self.__right]
        original_back = [row[:] for row in self.__back]
        original_left = [row[:] for row in self.__left]

        # turn the top side
        for i in range(3):
            for j in range(3):
                self.__top[j][2 - i] = original_top[i][j]

        # update the front side
        for i in range(3):
            self.__front[0][i] = original_right[0][i]

        # update the right side
        for i in range(3):
            self.__right[0][i] = original_back[0][i]

        # update the back side
        for i in range(3):
            self.__back[0][i] = original_left[0][i]

        # update the left side
        for i in range(3):
            self.__left[0][i] = original_front[0][i]

    def u_turn_prime(self) -> None:
        """Turn the top side of the cube counter-clockwise.
        This works by turning clockwise 3 times.
        """
        for i in range(3):
            self.u_turn()

    def d_turn(self) -> None:
        """Turn the bottom side of the cube clockwise.
        This works by saving the state of all the relevant sides,
        then reassigning items in the array by referencing parts of the original.
        """
        # Save the original states for reference
        original_bottom = [row[:] for row in self.__bottom]
        original_front = [row[:] for row in self.__front]
        original_right = [row[:] for row in self.__right]
        original_back = [row[:] for row in self.__back]
        original_left = [row[:] for row in self.__left]

        # turn the bottom side
        for i in range(3):
            for j in range(3):
                self.__bottom[j][2 - i] = original_bottom[i][j]

        # update the front side
        for i in range(3):
            self.__front[2][i] = original_left[2][i]

        # update the right side
        for i in range(3):
            self.__right[2][i] = original_front[2][i]

        # update the back side
        for i in range(3):
            self.__back[2][i] = original_right[2][i]

        # update the left side
        for i in range(3):
            self.__left[2][i] = original_back[2][i]

    def d_turn_prime(self) -> None:
        """Turn the bottom side of the cube counter-clockwise.
        This works by turning clockwise 3 times.
        """
        for i in range(3):
            self.d_turn()
    
    def r_turn(self) -> None:
        """Turn the right side of the cube clockwise.
        This works by saving the state of all the relevant sides,
        then reassigning items in the array by referencing parts of the original.
        """
        # Save the original states for reference
        original_right = [row[:] for row in self.__right]
        original_front = [row[:] for row in self.__front]
        original_bottom = [row[:] for row in self.__bottom]
        original_back = [row[:] for row in self.__back]
        original_top = [row[:] for row in self.__top]

        # turn the right side
        for i in range(3):
            for j in range(3):
                self.__right[j][2 - i] = original_right[i][j]

        # update the front side
        for i in range(3):
            self.__front[i][2] = original_bottom[i][2]

        # update the top side
        for i in range(3):
            self.__top[i][2] = original_front[i][2]

        # update the back side
        for i in range(3):
            self.__back[2 - i][0] = original_top[i][2]

        # update the bottom side
        for i in range(3):
            self.__bottom[i][2] = original_back[2 - i][0]
    
    def r_turn_prime(self) -> None:
        """Turn the right side of the cube counter-clockwise.
        This works by turning clockwise 3 times.
        """
        for i in range(3):
            self.r_turn()

    def l_turn(self) -> None:
        """Turn the left side of the cube clockwise.
        This works by saving the state of all the relevant sides,
        then reassigning items in the array by referencing parts of the original.
        """
        # Save the original states for reference
        original_left = [row[:] for row in self.__left]
        original_front = [row[:] for row in self.__front]
        original_bottom = [row[:] for row in self.__bottom]
        original_back = [row[:] for row in self.__back]
        original_top = [row[:] for row in self.__top]

        # turn the left side
        for i in range(3):
            for j in range(3):
                self.__left[j][2 - i] = original_left[i][j]

        # update the front side
        for i in range(3):
            self.__front[i][0] = original_top[i][0]

        # update the top side
        for i in range(3):
            self.__top[i][0] = original_back[2 - i][2]

        # update the back side
        for i in range(3):
            self.__back[2 - i][2] = original_bottom[i][0]

        # update the bottom side
        for i in range(3):
            self.__bottom[i][0] = original_front[i][0]

    def l_turn_prime(self) -> None:
        """Turn the left side of the cube counter-clockwise.
        This works by turning clockwise 3 times.
        """
        for i in range(3):
            self.l_turn()

    def __str__(self) -> str:
        """Return a visual representation of the cube.
        Works by looping through the different sides and adding them
        to the string.

        Returns:
            str: Visual representation of the cube, in a sideways t form
        """
        # the top 3 lines, representing the top side
        cube_string = ""
        for item in self.get_side("top"):
            cube_string += fg(0, 0, 0) + "X X X "
            for inner_item in item:
                cube_string += inner_item + " "
            cube_string += fg(0, 0, 0) + "X X X X X X\n"

        # the middle 3 lines, representing the left, front, right, and back sides
        for row in range(3):
            for item in self.get_side("left")[row]:
                cube_string += item + " "
            for item in self.get_side("front")[row]:
                cube_string += item + " "
            for item in self.get_side("right")[row]:
                cube_string += item + " "
            for item in self.get_side("back")[row]:
                cube_string += item + " "
            cube_string += "\n"

        # the bottom 3 lines, representing the bottom side
        for item in self.get_side("bottom"):
            cube_string += fg(0, 0, 0) + "X X X "
            for inner_item in item:
                cube_string += inner_item + " "
            cube_string += fg(0, 0, 0) + "X X X X X X\n"

        return cube_string
