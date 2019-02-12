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


class Pawn(Piece):
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
        super(Pawn, self).__init__(x, y, code, player)
        self.__isFirstMove = True

    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos):

        if self._player.getNumber() == 1:
            if self.__isFirstMove:
                if self._y + 2 == y or self._y + 1 == y and self._x == x:
                    self.__isFirstMove = False
                    return True
                else:
                    return False
            else:
                if self._y + 1 == y and self._x == x:
                    return True
                else:
                    return False
        else:
            if self.__isFirstMove:
                if self._y - 2 == y or self._y - 1 == y and self._x == x:
                    self.__isFirstMove = False
                    return True
                else:
                    return False
            else:
                if self._y - 1 == y and self.getX() == x and self._x == x:
                    return True
                else:
                    return False


if __name__ == '__main__':
    pass
