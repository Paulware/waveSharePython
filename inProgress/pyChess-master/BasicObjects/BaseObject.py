"""
    BaseObject class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com'
__modifiers__ = u''
__date__ = u''
__version__ = u'1.0.0'


# Importations


# Specific definitions


# Classes / Functions declaration


class BaseObject(object):
    """
    This class will be the base class for all the other class that will not
    be a process.
    ---------------------------------------------------------------------------
    Attributes :
        - _own_config = Config of the class
    """
    _own_config = {}

    def __init__(self, config):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        self._ownConfig = config