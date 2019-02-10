"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from BasicObjects.BaseState import BaseState
import pygame
# Specific definitions


# Classes / Functions declaration


class HomeState(BaseState):
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
        super(HomeState, self).__init__(cfg=cfg, main=main)


    def handle_events(self, events):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return : None.
        """
        for e in events:
            if e.type == pygame.MOUSEBUTTONUP:
                mx, my =  pygame.mouse.get_pos()
                for b in self._main.getButtons():
                    if mx > b.getX() and mx < b.getX() + b.getWidth() and my > b.getY() and my < b.getY() + b.getHeight():
                        b.action()
    def launch(self):
        pass

    def set_up(self):
        pass


if __name__ == '__main__':
    pass
    