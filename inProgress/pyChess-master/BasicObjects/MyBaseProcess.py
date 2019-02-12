"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com'
__modifiers__ = u''
__date__ = u''
__version__ = u'1.0.0'


# Importations
# Multiprocessing library
from multiprocessing import Process, Event


# Specific definitions


# Classes / Functions declaration


class MyBaseProcess(Process):
    """
    Base process class for all the process in the game
    ---------------------------------------------------------------------------
    Attributes :
        - _own_config : Self configuration of the object
        - _is_running  : True when the process is running.
    """
    _own_config = {}
    _is_running = False

    def __init__(self, config):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """

        # Initalize attributes
        self._ownConfig = config
        self._isRunning = False
        self._stopEvent = Event()

        # Calling mother class
        super(MyBaseProcess, self).__init__()


    def before_processing(self):
        """
        Method called before processing
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return :
            None

        """
        pass


    def after_processing(self):
        """
        Method called before processing
        -----------------------------------------------------------------------
        Arguments :

        -----------------------------------------------------------------------
        Return :
            None

        """
        pass

    def handle_self_events(self):
        if self._stopEvent.is_set():
            self._isRunning = False