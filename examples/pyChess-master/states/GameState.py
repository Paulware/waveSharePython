"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u'pyChess'
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'04/02/2019'
__version__ = u'1.0.0'

# Importations
from BasicObjects.BaseObject import BaseObject
from game.Piece import Piece
from game.Pawn import Pawn
from game.Rook import Rook
from game.Player import Player
from game.Knight import Knight
from game.Bishop import Bishop
from game.King import King
from game.Queen import Queen
from BasicObjects.BaseState import BaseState
import pygame

# Specific definitions
# CODE FOR PIECES
KING_CODE = 0
Piece.QUEEN_CODE = 1
Piece.ROOK_CODE = 2
Piece.BISHOP_CODE = 3
Piece.KNIGHT_CODE = 4
PAWN_CODE = 5


# Classes / Functions declaration


class GameState(BaseState):
    """
    This class is the main game class.
    ---------------------------------------------------------------------------
    Attributes :
        - __main : Main object
        - __grid : The grid of the game (8x8)
        - __player1 : The player 1 of the game
        - __player2 : The player 2 of the game
        - __piece_to_mouse : The piece that has been clicked dans that the player is moving
    """

    def __init__(self, cfg, main):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
            - cfg : Config of the class
            - main : Main class
        -----------------------------------------------------------------------
        Return : None.
        """
        super(GameState, self).__init__(cfg=cfg, main=main)
        self._main = main
        self.__grid = []
        self.__player1 = Player(cfg=self._ownConfig["players"]["1"], game=self, number=1)
        self.__player2 = Player(cfg=self._ownConfig["players"]["2"], game=self, number=2)
        self.__piece_to_mouse = None


    def set_up(self):
        """
        Method used to set_up everything
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        """
        # Set up the grid
        self.set_up_grid()

        # Set up pieces
        self.set_up_pieces()

        # start player
        self.__player1.set_playing(True)

    def launch(self):
        """
        Method called to launch the game
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.set_up()
    def set_up_grid(self):
        """
        Method called to set up the grid
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Setting the grid 8x8
        for i in range(8):
            self.__grid.append(i)

    def set_up_pieces(self):
        """
        Method called to set up the pieces
        It is not done with loop because it could need so much effort
        for nothing as the pieces are always the same and at the same square
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        pieces = []

        # Player 1
        pieces.append(Rook(y=0, x=0, code=Piece.ROOK_CODE, player=self.__player1))
        pieces.append(Knight(y=0, x=1, code=Piece.KNIGHT_CODE, player=self.__player1))
        pieces.append(Bishop(y=0, x=2, code=Piece.BISHOP_CODE, player=self.__player1))
        pieces.append(King(y=0, x=3, code=Piece.KING_CODE, player=self.__player1))
        pieces.append(Queen(y=0, x=4, code=Piece.QUEEN_CODE, player=self.__player1))
        pieces.append(Bishop(y=0, x=5, code=Piece.BISHOP_CODE, player=self.__player1))
        pieces.append(Knight(y=0, x=6, code=Piece.KNIGHT_CODE, player=self.__player1))
        pieces.append(Rook(y=0, x=7, code=Piece.ROOK_CODE, player=self.__player1))

        for i in range(8):
            pieces.append(Pawn(y=1, x=i, code=PAWN_CODE, player=self.__player1))
            pass
        self.__player1.setPieces(pieces)

        pieces = []

        # Player 2
        pieces.append(Rook(y=7, x=0, code=Piece.ROOK_CODE, player=self.__player2))
        pieces.append(Knight(y=7, x=1, code=Piece.KNIGHT_CODE, player=self.__player2))
        pieces.append(Bishop(y=7, x=2, code=Piece.BISHOP_CODE, player=self.__player2))
        pieces.append(King(y=7, x=3, code=Piece.KING_CODE, player=self.__player2))
        pieces.append(Queen(y=7, x=4, code=Piece.QUEEN_CODE, player=self.__player2))
        pieces.append(Bishop(y=7, x=5, code=Piece.BISHOP_CODE, player=self.__player2))
        pieces.append(Knight(y=7, x=6, code=Piece.KNIGHT_CODE, player=self.__player2))
        pieces.append(Rook(y=7, x=7, code=Piece.ROOK_CODE, player=self.__player2))
        pieces.append(Rook(y=7, x=8, code=Piece.ROOK_CODE, player=self.__player2))

        for i in range(8):
            pieces.append(Pawn(y=6, x=i, code=PAWN_CODE, player=self.__player2))

        self.__player2.setPieces(pieces)


    # GETTERS SETTERS
    def getGrid(self):
        return self.__grid

    def getPieces(self):
        return self.__player1.getPieces(), self.__player2.getPieces()

    def handle_events(self, events):
        """
        This method is used to handle events.
        -----------------------------------------------------------------------
        Arguments :
            - events : List of event from pygame.event.get()
        -----------------------------------------------------------------------
        Return : None.
        """
        # Event from pygame
        for event in events:
            # Window quit event
            if event.type == pygame.QUIT:
                self._main.stop_gui()

            # Click event
            elif event.type == pygame.MOUSEBUTTONUP:

                # Getting mouse coordinates
                mx, my = pygame.mouse.get_pos()
                # Checking if it's the first player is playing
                if self.__player1.is_playing():
                    # If it's him then we can check what to do with his click

                    played = self.check_clicked_pieces(self.__player1.getPieces(), mx, my, self.__player1.getNumber())
                    if played:
                        self.__player1.set_playing(False)
                        self.__player2.set_playing(True)
                else:
                    played = self.check_clicked_pieces(self.__player2.getPieces(), mx, my, self.__player2.getNumber())
                    if played:
                        self.__player1.set_playing(True)
                        self.__player2.set_playing(False)

    def checkmate(self):
        pass

    def check_clicked_pieces(self, pieces, mx, my, player_nb):
        """
        This method handle the click on the pieces.
        It will check which piece is clicked and how to handle it with
        the current player and pieces pos.
        -----------------------------------------------------------------------
        Arguments :
            - pieces : Current player pieces
            - mx : X pos of the mouse
            - my : Y pos of the mouse
            - player_nb : current number of the player
        -----------------------------------------------------------------------
        Return :
            - True : If the player moved his piece
            - False : If not
        """
        for player in (self.__player1, self.__player2):
            current_pl_pos, other_pl_pos = self.getPlayersPos(player_nb)

        # There we go for each piece of the player to check if he clicked on one
        for p in pieces:
            # Get the coordintes of the piece
            y = p.getY() * 62.5
            x = p.getX() * 62.5

            # We use x, y, mx, my to check if the current piece of the loop is being clicked and if there is no piece already
            # Selected
            if mx > x and mx < x + p.getWidth() and my > y and my < y + p.getWidth() and self.__piece_to_mouse == None and p.is_alive():
                # If so, we change the state of the piece
                p.selected()
                # And we keep a reference to the piece
                self.__piece_to_mouse = p
            # Same than above but with a piece already selected, so we need to check if the square is empty or if the is
            # an enemy on it
            elif mx > x and mx < x + p.getWidth() and my > y and my < y + p.getWidth() and self.__piece_to_mouse != None and p.is_alive():
                self.__piece_to_mouse.selected()

            # If there is already a piece selected
            elif self.__piece_to_mouse is not None:
                # If the selected piece is the current
                if p.is_selected():
                    # We get the clicked square
                    x, y = self.get_clicked_square(mx, my)

                    # We call the method of the piece to check if the moce is avaible
                    if p.is_move_avaible(x, y, current_pl_pos=current_pl_pos, other_pl_pos=other_pl_pos):
                        # Check if there is a kill
                        self.check_kill(x, y, player_nb)

                        # Update the pos of the piece
                        p.new_pos(x, y)
                        # Update the selected attribute of the piece
                        p.selected()
                        # Remove the reference
                        self.__piece_to_mouse = None
                        return True

                    # If the move is not avaible we reset put back the piece where it belongs
                    p.selected()
                    self.__piece_to_mouse = None
                    return False
        return False

    def getPlayersPos(self, player_nb):
        """
        Method used to get the player pieces pos
        -----------------------------------------------------------------------
        Arguments :
            - player_nb : Current number of the player
        -----------------------------------------------------------------------
        Return :
            - current_pl_pos : list with current player pieces pos
            - other_pl_pos : list with the player that is not playing pieces pos
        """
        current_pl_pos = []
        other_pl_pos = []

        # Setting up var to loop
        if player_nb == 1:
            player = self.__player1
            other_player = self.__player2
        else:
            player = self.__player2
            other_player = self.__player1

        # Adding pieces to each list
        for p in player.getPieces():
            current_pl_pos.append(p.getPos())

        for p in other_player.getPieces():
            other_pl_pos.append(p.getPos())

        return current_pl_pos, other_pl_pos

    def check_kill(self, x, y, player_nb):
        """
        Method used to check if there is a kill
        -----------------------------------------------------------------------
        Arguments :
            - x : X of the next square
            - y : Y of the next square
        -----------------------------------------------------------------------
        Return : None.
        """
        # Going through all pieces
        for pl in (self.__player1, self.__player2):
            for i, piece in enumerate(pl.getPieces()):
                # If the pieces that might be killed is an enemy piece
                if piece.getX() == x and piece.getY() == y and piece.getPlayerNumber() != player_nb:
                    # If there is a kill then we leave the loop
                    self.kill_piece(piece.getPlayerNumber(), i)
                    break

    def kill_piece(self, nb_player, piece):
        """
        Method used to kill a piece
        -----------------------------------------------------------------------
        Arguments :
            - nb_player : Number of the piece's player
            - piece : Piece that have to be kill
        -----------------------------------------------------------------------
        Return : None.
        """
        if nb_player == 1:
            self.__player1.kill_piece(piece)
        else:
            self.__player2.kill_piece(piece)

    def get_clicked_square(self, x, y):
        """
        Method that calculate the square from coordinate (x, y)
        -----------------------------------------------------------------------
        Arguments :
            - x : X coordinate
            - y : Y coordinate
        -----------------------------------------------------------------------
        Return :
            - x : X within the grid (from 0 to 7)
            - y : Y within the grid (from 0 to 7)
        """
        x = int(x / 62.5)
        y = int(y / 62.5)
        return x, y


if __name__ == '__main__':
    g = GameState(None, None)
    g.set_up_grid()
