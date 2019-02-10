"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from BasicObjects.BaseObject import BaseObject

# Specific definitions


# Classes / Functions declaration


class Player(BaseObject):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, cfg, game, number):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(Player, self).__init__(config=cfg)
        self.__game = game
        self.__pieces = None
        self.__number = number
        self.__playing = False


    def is_playing(self):
        return self.__playing

    def set_playing(self, p):
        self.__playing = p
    def getPieces(self):
        return self.__pieces

    def setPieces(self, p):
        self.__pieces = p

    def getNumber(self):
        return self.__number

    def kill_piece(self, i):
        # print("Player / Killed : \n", self.__pieces[i])
        self.__pieces.pop(i)




if __name__ == '__main__':
    pass
    