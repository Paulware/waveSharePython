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


class Rook(Piece):
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
        super(Rook, self).__init__(x, y, code, player)

    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :

        -----------------------------------------------------------------------
        Return :
            None
        """
        current_pl_pos.remove(self.getPos())
        if (x,y) in other_pl_pos:
            other_pl_pos.remove((x,y))
        right = None
        up = None
        if self.getX() == x and self.getY() == y:
            return False

        elif self.getY() == y and self.getX() != x:
            if self.getX() - x < 0 :
                right = True
            elif self.getX() -x > 0:
                right= False

            if right:
                for i in range(0, self.getX() - x - 1, - 1):
                    next_pos =(self.getX() - i, self.getY())
                    if next_pos in current_pl_pos or next_pos in other_pl_pos:
                        return False

            else:
                for i in range(0, self.getX() - x + 1, 1):
                    next_pos = (self.getX() - i, self.getY())
                    if  next_pos in current_pl_pos or next_pos in other_pl_pos:
                        return False
        elif self.getY() != y and self.getX() == x:

            if self.getY() - y < 0:
                up = False
            elif self.getY() - y > 0:
                up = True

            if up:
                for i in range(0, self.getY() - y + 1, 1):
                    # print("test i : ", i)
                    # print((self.getX(), self.getY() - i))
                    next_pos = (self.getX(), self.getY() - i)
                    if next_pos in current_pl_pos or next_pos in other_pl_pos:
                        return False
                        # pass
            else:
                for i in range(0, self.getY() - y - 1, - 1):
                    print("test i : ", i)
                    print((self.getX(), self.getY() - i))
                    next_pos = (self.getX(), self.getY() - i)
                    if  next_pos in current_pl_pos or next_pos in other_pl_pos:
                        return False
                        # pass
        else:
            return False
        return True

    def check_jump(self, x, y, piece_pos):
        pass


if __name__ == '__main__':
    pass
