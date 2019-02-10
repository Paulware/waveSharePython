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


class BaseCanvas(pygame.Surface):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, width, height, gui, master, cfg):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(BaseCanvas, self).__init__(size=(width, height))
        self._ownConfig = cfg
        self._width = width
        self._height = height
        self._gui = gui
        self._master = master
        self._bg_img = None

    def draws(self):
        pass

    def set_up(self):
        pass

    def set_up_bc_img(self):
        pass


if __name__ == '__main__':
    pass
    