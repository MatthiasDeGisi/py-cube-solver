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
        self.__front = [[G, G, G], [G, G, G], [G, G, G]]
        self.__back = [[B, B, B], [B, B, B], [B, B, B]]
        self.__top = [[W, W, W], [W, W, W], [W, W, W]]
        self.__bottom = [[Y, Y, Y], [Y, Y, Y], [Y, Y, Y]]
        self.__right = [[R, R, R], [R, R, R], [R, R, R]]
        self.__left = [[O, O, O], [O, O, O], [O, O, O]]

    def get_side(self, side: str) -> list:
        """Return the array representation of a side.

        Args:
            side (str): the side to return

        Returns:
            list: the representation of the side
        """
        if side == "front":
            return self.__front
        if side == "back":
            return self.__back
        if side == "top":
            return self.__top
        if side == "bottom":
            return self.__bottom
        if side == "right":
            return self.__right
        if side == "left":
            return self.__left

    def __str__(self) -> str:
        cube_string = ""
        for item in self.get_side("top"):
            cube_string += fg(0, 0, 0) + "X X X "
            for inner_item in item:
                cube_string += inner_item + " "
            cube_string += fg(0, 0, 0) + "X X X X X X\n"

        for row in range(3):
            for item in self.get_side("left")[row]:
                cube_string += item + " "
            for item in self.get_side("front")[row]:
                cube_string += item + " "
            for item in self.get_side("left")[row]:
                cube_string += item + " "
            for item in self.get_side("back")[row]:
                cube_string += item + " "
            cube_string += "\n"

        for item in self.get_side("bottom"):
            cube_string += fg(0, 0, 0) + "X X X "
            for inner_item in item:
                cube_string += inner_item + " "
            cube_string += fg(0, 0, 0) + "X X X X X X\n"

        return cube_string