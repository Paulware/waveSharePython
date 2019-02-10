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


class BaseState(BaseObject):
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
        super(BaseState, self).__init__(config=cfg)
        self._main = main

    def set_up(self):
        pass
    def launch(self):
        pass
    def handle_events(self, events):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return : None.
        """
        for e in events:
            pass


if __name__ == '__main__':
    pass
    