"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from display.TextToDisp import TextToDisp
import pygame
# Specific definitions


# Classes / Functions declaration


class Button(object):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, x, y, w, h, color, text, master):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        self.__x = x
        self.__y = y
        self.__width = w
        self.__height = h
        self.__color = color
        self.__text = text
        self.__master = master


    def action(self):
        self.__master.set_state("game")

    def set_up(self):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return :
            None
        """
        font = "res/font/good_time.ttf"
        self.__text = TextToDisp(font=font,
                                  size=20,
                                  text=self.__text,
                                  x=0, y=0, color=(255, 255, 255))

        self.__text.set_up()

        origin = self.getX()
        x = origin + (self.getWidth() - self.__text.getText().get_width()) / 2
        y_origin = self.getY()
        y = y_origin + (self.getHeight() - self.__text.getText().get_height()) / 2
        self.__text.setX(x)
        self.__text.setY(y)

# GETTERS / SETTERS

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getRect(self):
        return pygame.Rect(self.__x, self.__y, self.__width, self.__height)

    def getColor(self):
        return self.__color

    def getText(self):
        return self.__text

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height


if __name__ == '__main__':
    pass
