"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
import pygame

# Specific definitions


# Classes / Functions declaration


class TextToDisp(object):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, font, size, text, x, y, color):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(TextToDisp, self).__init__()
        self.__font = font
        self.__size = size
        self.__text = text
        self.__x = x
        self.__y = y
        self.__color = color

    def set_up(self):
        font = pygame.font.Font(self.getFont(), self.getSize())

        self.__text = font.render(self.getText(), True, self.getColor())



    # GETTERS / SETTERS #

    def getFont(self):
        return self.__font

    def getSize(self):
        return self.__size

    def getText(self):
        return self.__text

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getColor(self):
        return self.__color

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

if __name__ == '__main__':
    pass
    