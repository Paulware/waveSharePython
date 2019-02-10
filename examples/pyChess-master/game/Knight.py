"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from game.Piece import Piece


# Specific definitions


# Classes / Functions declaration


class Knight(Piece):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :

    """

    def __init__(self, x, y, code, player):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.

        """
        super(Knight, self).__init__(x, y, code, player)

    def check_jump(self, x, y, other_pc_pos):
        delta_x = self.getX() - x
        delta_y = self.getY() - y

        # if delta_x < x:
        #     first_direction = "right"
        #
        # first_direction = ""
        #
        # if delta_x < 1:
        #     delta_x_stride = -1
        # else:
        #     delta_x_stride = 1


        abs_deltx = abs(delta_x)
        abs_delty = abs(delta_y)
        if self.getY() > y and abs_delty > abs_deltx :
            print("UP -2")
            if self.getX() > x:
                print("LEFT - 1")
            elif self.getX() < x:
                print("LEFT + 1")
        elif self.getY() < y and abs_delty > abs_deltx:
            print("DOWN + 2")
            if self.getX() > x :
                print("LEFT - 1")
            elif self.getX() < x:
                print("LEFT + 1")
        elif self.getX() > x and abs_deltx > abs_delty:
            print("LEFT - 2")
            if self.getY() > y:
                print("UP - 1")
            elif self.getY() < y:
                print("UP + 1")
        elif self.getX() < x and abs_deltx > abs_delty:
            print("RIGHT +2")
            if self.getY() > y:
                print("UP - 1")
            elif self.getY() < y:
                print("DOWN +1")

    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos):

        print((x,y))
        # for i in other_pl_pos:
        #     print(i)
        if (x, y) in current_pl_pos:
            return False

        if self._y + 2 == y and self._x + 1 == x:
            return True
        elif self._y + 2 == y and self._x - 1 == x:
            return True
        elif self._y - 2 == y and self._x - 1 == x:
            return True
        elif self._y - 2 == y and self._x + 1 == x:
            return True
        elif self._y - 1 == y and self._x - 2 == x:
            return True
        elif self._y + 1 == y and self._x - 2 == x:
            return True
        elif self._y - 1 == y and self._x + 2 == x:
            return True
        elif self._y + 1 == y and self._x + 2 == x:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
