"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from os import sep
import pygame
# Specific definitions


# Classes / Functions declaration


class Piece(object):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    # Const TODO: Check why it's not working when it outside the class
    KING_CODE = 0
    QUEEN_CODE = 1
    ROOK_CODE = 2
    BISHOP_CODE = 3
    KNIGHT_CODE = 4
    PAWN_CODE = 5

    # Player number for the colors
    NUMBER_1_COLOR = "w"
    NUMBER_2_COLOR = "b"


    def __init__(self, x, y, code, player):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        self._x = x
        self._y = y
        self._code = code
        self._player = player
        self._img = None
        self._width = 62.5
        self._selected = False
        self._alive = True
        self._can_jump = False
        self.set_can_jump()

    def __str__(self):
        strr = "pos : [" + str(self._x) + "," + str(self._y) + "] \n"
        strr += "player : " + str(self._player.getNumber())
        strr += "------------------------------"
        return(strr)

    def set_can_jump(self):
        if self.getCode() == self.KNIGHT_CODE:
            self._can_jump = True
        else:
            self._can_jump = False

    def set_img(self):
        # Method used to set_up the img of the piece
        path = "res" + sep + "img" + sep + self.code_to_str() + "-" + self.getColor() + ".png"
        self._img = pygame.image.load(path)
        self._img = pygame.transform.scale(self._img, (int(62.5 - 15), int(62.5 - 15)))


    def getColor(self):
        if self._player.getNumber() == 1:
            return self.NUMBER_1_COLOR
        else:
            return self.NUMBER_2_COLOR

    def selected(self):
        if self._selected:
            self._selected = False
        else:
            self._selected = True

    def is_selected(self):
        return self._selected

    def getWidth(self):
        return self._width

    def getCode(self):
        return self._code

    def getImg(self):
        return self._img

    def getX(self):
        return self._x

    def getPos(self):
        return self._x, self._y

    def getY(self):
        return self._y

    def check_jump(self, x, y, other_pc_pos):

        delta_y = self.getY() - y
        delta_x = self.getX() - x
        print("ENTER LOOP DELTA")
        if delta_y < 0:
            stride_y = -1
        else:
            stride_y = 1

        if delta_x < 0:
            stride_x = -1
        else:
            stride_x = 1

        for pos in other_pc_pos:
            for i in range(0, delta_y, stride_y):
                if (self.getX() , self.getY() + i) == pos and pos != self.getPos():
                    print("Oups")

            for i in range(0, delta_x, stride_x):
                if (self.getX() + i, self.getY()) == pos and pos != self.getPos():
                    print("oups2")

        print("-----------------------------------------")
        print("DELAT X : ", delta_x, "DELTA Y :", delta_y)
        print("-----------------------------------------")
    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos):
        pass

    def new_pos(self,x, y):
        self._x = x
        self._y = y

    def getPlayerNumber(self):
        return self._player.getNumber()

    def is_alive(self):
        return self._alive

    def code_to_str(self):
        if self._code == 0:
            return "king"
        elif self._code == 1:
            return "queen"
        elif self._code == 2:
            return "rook"
        elif self._code == 3:
            return "bishop"
        elif self._code == 4:
            return "knight"
        else:
            return "pawn"

if __name__ == '__main__':
    pass
    