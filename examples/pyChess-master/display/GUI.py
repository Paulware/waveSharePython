"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'28/01/19'
__version__ = u'1.0.0'

# Importations
from display.GameCanvas import GameCanvas
from display.HomeCanvas import HomeCanvas
import pygame
from BasicObjects.MyBaseProcess import MyBaseProcess
import time


# Specific definitions


# Classes / Functions declaration


class GUI(MyBaseProcess):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, cfg, main):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(GUI, self).__init__(cfg)
        self._ownConfig = cfg
        self.__window = None
        self.__main = main
        self.__frame = None

    def set_up(self):
        pygame.init()
        self.__window = pygame.display.set_mode((self._ownConfig["def_w"], self._ownConfig["def_h"]))
        self.__frame = HomeCanvas(self, self._ownConfig["def_w"], self._ownConfig["def_h"], gui=self, cfg=self._ownConfig["canvas"]["home"])
        self.__frame.set_up()
        self._isRunning = True

    def getWidth(self):
        return self._ownConfig["def_w"]

    def getHeight(self):
        return self._ownConfig["def_h"]

    def set_game_canvas(self):
        self.__frame = GameCanvas(self, self._ownConfig["def_w"], self._ownConfig["def_h"], gui=self, cfg=self._ownConfig["canvas"]["game"])
        self.__frame.set_up()

    def run(self):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return :
            None
        """
        self.set_up()

        while self._isRunning:
            self.__frame.draws()
            self.__window.blit(self.__frame, (0, 0))
            pygame.display.flip()
            super(GUI, self).handle_self_events()
            self.__main.handle_events(pygame.event.get())
            time.sleep(0.001)

    def getGrid(self):
        return self.__main.getGrid()

    def getPieces(self):
        return self.__main.getPieces()

    def set_stop_event(self):
        self._stopEvent.set()

    def getWindow(self):
        return self.__window

    def gerFrame(self):
        return self.__frame

    def getButtons(self):
        return self.__frame.getButtons()

    def set_state(self, state):
        self.__main.set_state(state)

if __name__ == '__main__':
    pass
