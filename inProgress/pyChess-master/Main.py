"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u'Chess'
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'27/01/2019'
__version__ = u'1.0.0'


# Importations
import json
from display.GUI import GUI
from states.GameState import GameState
import importlib
import pygame
# Specific definitions
IMG_PATH = "res/img"

# Classes / Functions declaration


class Main(object):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(Main, self).__init__()
        self.__allConfig = None
        self.__gui = None
        self.__grid = []
        self.__state = None
        self.__game = None
        pygame.init()
        # print(self.__state)
        # import sys
        # sys.exit()

    def setUp(self):
        # Loading the general config of the game
        self.loadConfig()
        self.set_state("home")

        # Loading GUI
        self.__gui = GUI(self.__allConfig["gui"], self)


    def launch(self):
        # self.__gui.set_canvas("home")
        self.__gui.start()

    def loadConfig(self):
        cfg_file = open("./config.json")
        self.__allConfig = json.load(cfg_file, encoding='utf-8')
        cfg_file.close()


    def launch_game(self):
        # Game
        self.__state = GameState(self.__allConfig["game"], self)
        self.__state.launch()

# GETTERS SETTERS


    def set_state(self, new_state):

        class_name = new_state.capitalize() + "State"
        if type(self.__state).__name__ != class_name:
            # Creating dynamically the state class
            try:
                # Import library
                module = importlib.import_module("states." + class_name)

                # Get the class object
                state_class = None

                if class_name:
                    state_class = getattr(module, class_name)
                    # Setting the current state got in parameters as the new state

                    self.__state = state_class(main=self, cfg=self.__allConfig["states"][new_state.lower()])
                    self.__state.set_up()
                    self.__state.launch()
                    self.__gui.set_game_canvas()

            except Exception as exc:
                print(
                    "Can't import : {lib}".format(lib=class_name))
                print(
                    "Error message : {msg}".format(msg=exc.args))

    def getGrid(self):
        return self.__state.getGrid()

    def getButtons(self):
        return self.__gui.getButtons()

    def set_canvas(self, state):
        self.__gui.set_game_canvas()

    def getPieces(self):
        return self.__state.getPieces()

    def handle_events(self, events):
        if self.__state != None:
            self.__state.handle_events(events)


    def stop_gui(self):
        self.__gui.set_stop_event()

    def getState(self):
        return self.__state

if __name__ == '__main__':
    main = Main()
    main.setUp()
    main.launch()
    