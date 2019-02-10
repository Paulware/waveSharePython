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


class King(Piece):
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
        super(King, self).__init__(x, y, code, player)
        self.__isFirstMove = True

    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos):

        if self.getX() - x < 0:
            going_right = True
        else:
            going_right = False

        if self.getY() - y < 0:
            going_up = False
        else:
            going_up = True

        if -1 <= self.getX() - x <= 1 and self.getY() == y:
            if going_right and (self.getX() + 1, self.getY()) not in current_pl_pos:
                return True
            elif not going_right and (self.getX() - 1, self.getY()) not in current_pl_pos:
                return True

        elif -1 <= self.getY() - y <= 1 and self.getX() == x:
            if going_up and (self.getX(), self.getY() - 1) not in current_pl_pos:
                return True
            elif not going_up and (self.getX(), self.getY() + 1) not in current_pl_pos:
                return True

if __name__ == '__main__':
    pass
