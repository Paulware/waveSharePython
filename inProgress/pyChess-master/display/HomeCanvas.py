"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from BasicObjects.BaseCanvas import BaseCanvas
import pygame
from display.TextToDisp import TextToDisp
from display.Button import Button
# Specific definitions


# Classes / Functions declaration


class HomeCanvas(BaseCanvas):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :

    """

    def __init__(self, master, width, height, gui, cfg):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.

        """
        super(HomeCanvas, self).__init__(width=width, height=height, gui=gui, master=master, cfg=cfg)
        self.__bg_color = (255, 255, 255)
        self.__title = ""
        self.__buttons = []

    def draws(self):
        """
        Method used to draw all images needed
        -----------------------------------------------------------------------
        Arguments :

        -----------------------------------------------------------------------
        Return :
            None
        """
        # self.fill((255, 255, 255))
        self.draw_bg()
        self.draw_title()
        self.draw_buttons()

    def set_up_title(self):
        font = "res/font/good_time.ttf"
        self.__title = TextToDisp(font=font,
                                  size=60,
                                  text="pyChess",
                                  x=100,
                                  y=100, color=(0,0,0))

        self.__title.set_up()

        x = (self._width - self.__title.getText().get_width()) / 2
        y =  self.__title.getText().get_height() + 10

        self.__title.setX(x)
        self.__title.setY(y)


    def set_up_buttons(self):
        b_w = 200
        b_h = 50
        button = Button(x=0, y=0, w=b_w, h=b_h, color=(0,0,0), text="Settings", master=self)

        x = (self.get_width() - b_w) / 2
        y = self.get_height() - 110
        button.setX(x)
        button.setY(y)
        button.set_up()

        self.__buttons.append(button)

        button = Button(x=0, y=0, w=b_w, h=b_h, color=(0, 0, 0), text="Play !", master=self)

        x = (self.get_width() - b_w) / 2
        y = self.get_height() - 110 - b_h - 10
        button.setX(x)
        button.setY(y)
        button.set_up()

        self.__buttons.append(button)





    def draw_buttons(self):
        for b in self.__buttons:
            pygame.draw.rect(self, b.getColor(), b.getRect())
            self.blit(b.getText().getText(), (b.getText().getX(), b.getText().getY()))

    def draw_title(self):
        self.blit(self.__title.getText(),
                    (self.__title.getX(), self.__title.getY()))


    def set_up(self):
        """
        Setting up the images and everything else
        :return:
        """
        self.set_up_title()
        self.set_up_buttons()
    def draw_bg(self):
        self.fill(self.__bg_color)

    def getButtons(self):
        return self.__buttons

    def set_state(self, state):
        print(self._master)
        self._master.set_state(state)

if __name__ == '__main__':
    pass
