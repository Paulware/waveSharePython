import random, sys, pygame, time, copy
from pygame.locals import *
import buttonClass
import os
import sys

buttons = buttonClass.ButtonsClass(0.2)

FPS = 10 # frames per second to update the screen
WINDOWWIDTH = 800 # width of the program's window, in pixels
WINDOWHEIGHT = 600 # height in pixels
SPACESIZE = 50 # width & height of each space on the board, in pixels
BOARDWIDTH = 8 # how many columns of spaces on the game board
BOARDHEIGHT = 8 # how many rows of spaces on the game board
WHITE_TILE = 'WHITE_TILE' # an arbitrary but unique value
BLACK_TILE = 'BLACK_TILE' # an arbitrary but unique value
EMPTY_SPACE = 'EMPTY_SPACE' # an arbitrary but unique value
HINT_TILE = 'HINT_TILE' # an arbitrary but unique value
ANIMATIONSPEED = 25 # integer from 1 to 100, higher is faster animation
mouseX = 5 # start mouse block
mouseY = 5 # start mouse block
BOXSIZE = 50 # size of box height & width in pixels

# Amount of space on the left & right side (XMARGIN) or above and below
# (YMARGIN) the game board, in pixels.
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2)

#              R    G    B
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
GREEN      = (  0, 155,   0)
BRIGHTBLUE = (  0,  50, 255)
BROWN      = (174,  94,   0)
RED        = (255,   0,   0)

TEXTBGCOLOR1 = BRIGHTBLUE
TEXTBGCOLOR2 = GREEN
GRIDLINECOLOR = BLACK
TEXTCOLOR = WHITE
HINTCOLOR = BROWN

print ("starting menuGrid?");

def leftTopCoordsOfBox(boxx, boxy):
    left = (boxx * BOXSIZE) + XMARGIN
    top  = (boxy * BOXSIZE) + YMARGIN
    return (left, top)
    
def drawMouse ():
    global DISPLAYSURF
    global mouseX
    global mouseY
    global RED
    half = int(BOXSIZE * 0.5)  # syntactic sugar
    left, top = leftTopCoordsOfBox(mouseX, mouseY) # get pixel coords from board coords    
    pygame.draw.polygon(DISPLAYSURF, RED, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    pygame.display.update()
       
def handleButton(data):
    global mouseX
    global mouseY
    global BOXSIZE
    global YMARGIN
    global XMARGIN
    
    BOARDWIDTH = 8 # number of columns of icons
    BOARDHEIGHT = 8 # number of rows of icons
    
    if buttons.checkKey ("Start"):
        data['quit'] = True

    if buttons.checkKey ("Up"):
        if (mouseY > 0): 
            mouseY = mouseY - 1
       
    if buttons.checkKey ("Down"):
        if (mouseY + 1 < BOARDHEIGHT): 
            mouseY = mouseY + 1
       
    if buttons.checkKey ("Left"):
        if (mouseX > 0): 
            mouseX = mouseX - 1
       
    if buttons.checkKey ("Right"):
        if (mouseX + 1< BOARDWIDTH): 
            mouseX = mouseX + 1
           
    if buttons.checkKey ("A"):    
        data['mouseClicked'] = True
        left, top = leftTopCoordsOfBox(1, 1)
        data ['movexy'] = (mouseX,mouseY)
        data['mousex'] = (mouseX * BOXSIZE) + XMARGIN
        data['mousey'] = (mouseY * BOXSIZE) + YMARGIN
       


def main():
    global MAINCLOCK, DISPLAYSURF, FONT, BIGFONT, BGIMAGE
    global mousex, mousey
    
    mousex, mousey = leftTopCoordsOfBox (mouseX, mouseY)

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Flippy')
    FONT = pygame.font.Font('freesansbold.ttf', 16)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 32)

    # Set up the background image.
    boardImage = pygame.image.load('flippyboard.png')
    # Use smoothscale() to stretch the board image to fit the entire board:
    boardImage = pygame.transform.smoothscale(boardImage, (BOARDWIDTH * SPACESIZE, BOARDHEIGHT * SPACESIZE))
    boardImageRect = boardImage.get_rect()
    boardImageRect.topleft = (XMARGIN, YMARGIN)
    BGIMAGE = pygame.image.load('flippybackground.png')
    # Use smoothscale() to stretch the background image to fit the entire window:
    BGIMAGE = pygame.transform.smoothscale(BGIMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
    BGIMAGE.blit(boardImage, boardImageRect)

    # Run the main game.
    while True:
        if runGame() == False:
            break

def runGame():
    global mousex
    global mousey
    global DISPLAYSURF
    global MAINCLOCK

    tetrisSurf = FONT.render('Tetris', True, TEXTCOLOR, TEXTBGCOLOR2)
    tetrisRect = tetrisSurf.get_rect()
    tetrisRect.topright = (245, 110)   

    othelloSurf = FONT.render('Othello', True, TEXTCOLOR, TEXTBGCOLOR2)
    othelloRect = othelloSurf.get_rect()
    othelloRect.topright = (245, 160)   
    


    # Reset the board and game.
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    showHints = False
    turn = random.choice(['computer', 'player'])

    # Draw the starting board and ask the player what color they want.
    drawBoard(mainBoard)
    #playerTile, computerTile = enterPlayerTile()

    # Make the Surface and Rect objects for the "New Game" and "Hints" buttons
    newGameSurf = FONT.render('New Game', True, TEXTCOLOR, TEXTBGCOLOR2)
    newGameRect = newGameSurf.get_rect()
    newGameRect.topright = (WINDOWWIDTH - 8, 10)
    hintsSurf = FONT.render('Hints', True, TEXTCOLOR, TEXTBGCOLOR2)
    hintsRect = hintsSurf.get_rect()
    hintsRect.topright = (WINDOWWIDTH - 8, 40)
    drawMouse ()
    print ("Waiting for left right up down on players turn")
    while True: # main game loop
        print ("Players turn") 
        if buttons.checkKey ("Start"):
            print ("Start button detected, data[quit] = True" )
            data['quit'] = True
            break
            
        movexy = None
        while movexy == None:
            # Keep looping until the player clicks on a valid space.

            # Determine which board data structure to use for display.
            if showHints:
                boardToDraw = getBoardWithValidMoves(mainBoard, playerTile)
            else:
                boardToDraw = mainBoard

            data = {'mouseClicked':False,'quit':False,
                    'mousex':mousex,'mousey':mousey}
            mousex = data ['mousex']
            mousey = data ['mousey']
            handleButton(data)
            drawMouse()
            if (data['quit'] ):
                pygame.quit()
            
            if (data['mouseClicked']): 
                print ("Mouse was clicked [x,y]: [" + str(mousex) + "," + str(mousey) + "]")                
                if newGameRect.collidepoint( (mousex, mousey) ):
                    # Start a new game
                    return True
                elif hintsRect.collidepoint( (mousex, mousey) ):
                    # Toggle hints mode
                    showHints = not showHints
                # movexy is set to a two-item tuple XY coordinate, or None value
                #movexy = getSpaceClicked(mousex, mousey)
                movexy = data['movexy']
                print ("Got space clicked :" + str(movexy))
                if (movexy[0] == 0) and (movexy[1] == 0):
                   print ("Run tetris")
                   pygame.quit()
                   os.system ("python tetris.py")
                   pygame.init()
                   MAINCLOCK = pygame.time.Clock()
                   DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))                   
                   

            # Draw the game board.
            drawBoard(boardToDraw)
            #drawInfo(boardToDraw, playerTile, computerTile, turn)

            # Draw the "New Game" and "Hints" buttons.
            DISPLAYSURF.blit(newGameSurf, newGameRect)
            DISPLAYSURF.blit(hintsSurf, hintsRect)
            DISPLAYSURF.blit(tetrisSurf, tetrisRect)
            DISPLAYSURF.blit(othelloSurf, othelloRect)

            MAINCLOCK.tick(FPS)
            pygame.display.update()

       

    # Display the final score.
    drawBoard(mainBoard)

    textSurf = FONT.render(text, True, TEXTCOLOR, TEXTBGCOLOR1)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(textSurf, textRect)

    # Display the "Play again?" text with Yes and No buttons.
    text2Surf = BIGFONT.render('Play again? (A=yes,B=no)', True, TEXTCOLOR, TEXTBGCOLOR1)
    text2Rect = text2Surf.get_rect()
    text2Rect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 50)

    while True:
    
        # Process events until the user clicks on Yes or No.
        if buttons.checkKey ("B"):
           return False
           
        if button.checkKey ("A"):
           return True
           
        DISPLAYSURF.blit(textSurf, textRect)
        DISPLAYSURF.blit(text2Surf, text2Rect)
        DISPLAYSURF.blit(yesSurf, yesRect)
        DISPLAYSURF.blit(noSurf, noRect)
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def translateBoardToPixelCoord(x, y):
    return XMARGIN + x * SPACESIZE + int(SPACESIZE / 2), YMARGIN + y * SPACESIZE + int(SPACESIZE / 2)


def animateTileChange(tilesToFlip, tileColor, additionalTile):
    # Draw the additional tile that was just laid down. (Otherwise we'd
    # have to completely redraw the board & the board info.)
    if tileColor == WHITE_TILE:
        additionalTileColor = WHITE
    else:
        additionalTileColor = BLACK
    additionalTileX, additionalTileY = translateBoardToPixelCoord(additionalTile[0], additionalTile[1])
    pygame.draw.circle(DISPLAYSURF, additionalTileColor, (additionalTileX, additionalTileY), int(SPACESIZE / 2) - 4)
    pygame.display.update()

    for rgbValues in range(0, 255, int(ANIMATIONSPEED * 2.55)):
        if rgbValues > 255:
            rgbValues = 255
        elif rgbValues < 0:
            rgbValues = 0

        if tileColor == WHITE_TILE:
            color = tuple([rgbValues] * 3) # rgbValues goes from 0 to 255
        elif tileColor == BLACK_TILE:
            color = tuple([255 - rgbValues] * 3) # rgbValues goes from 255 to 0

        for x, y in tilesToFlip:
            centerx, centery = translateBoardToPixelCoord(x, y)
            pygame.draw.circle(DISPLAYSURF, color, (centerx, centery), int(SPACESIZE / 2) - 4)
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def drawBoard(board):
    # Draw background of board.
    DISPLAYSURF.blit(BGIMAGE, BGIMAGE.get_rect())

    # Draw grid lines of the board.
    for x in range(BOARDWIDTH + 1):
        # Draw the horizontal lines.
        startx = (x * SPACESIZE) + XMARGIN
        starty = YMARGIN
        endx = (x * SPACESIZE) + XMARGIN
        endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))
    for y in range(BOARDHEIGHT + 1):
        # Draw the vertical lines.
        startx = XMARGIN
        starty = (y * SPACESIZE) + YMARGIN
        endx = XMARGIN + (BOARDWIDTH * SPACESIZE)
        endy = (y * SPACESIZE) + YMARGIN
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))

    


'''
def drawInfo(board, playerTile, computerTile, turn):
    # Draws scores and whose turn it is at the bottom of the screen.
    scores = getScoreOfBoard(board)
    scoreSurf = FONT.render("Player Score: %s    Computer Score: %s    %s's Turn" % (str(scores[playerTile]), str(scores[computerTile]), turn.title()), True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.bottomleft = (10, WINDOWHEIGHT - 5)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
'''

def resetBoard(board):
    # Blanks out the board it is passed, and sets up starting tiles.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            board[x][y] = EMPTY_SPACE

    # Add starting pieces to the center
    board[3][3] = WHITE_TILE
    board[3][4] = BLACK_TILE
    board[4][3] = BLACK_TILE
    board[4][4] = WHITE_TILE


def getNewBoard():
    # Creates a brand new, empty board data structure.
    board = []
    for i in range(BOARDWIDTH):
        board.append([EMPTY_SPACE] * BOARDHEIGHT)

    return board


def isValidMove(board, tile, xstart, ystart):
    # Returns False if the player's move is invalid. If it is a valid
    # move, returns a list of spaces of the captured pieces.
    if board[xstart][ystart] != EMPTY_SPACE or not isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = tile # temporarily set the tile on the board.

    if tile == WHITE_TILE:
        otherTile = BLACK_TILE
    else:
        otherTile = WHITE_TILE

    tilesToFlip = []
    # check each of the eight directions:
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # The piece belongs to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break # break out of while loop, continue in for loop
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse
                # direction until we reach the original space, noting all
                # the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = EMPTY_SPACE # make space empty
    if len(tilesToFlip) == 0: # If no tiles flipped, this move is invalid
        return False
    return tilesToFlip


def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x < BOARDWIDTH and y >= 0 and y < BOARDHEIGHT


def getBoardWithValidMoves(board, tile):
    # Returns a new board with hint markings.
    dupeBoard = copy.deepcopy(board)

    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = HINT_TILE
    return dupeBoard


def getValidMoves(board, tile):
    # Returns a list of (x,y) tuples of all valid moves.
    validMoves = []

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append((x, y))
    return validMoves


def getScoreOfBoard(board):
    # Determine the score by counting the tiles.
    xscore = 0
    oscore = 0
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == WHITE_TILE:
                xscore += 1
            if board[x][y] == BLACK_TILE:
                oscore += 1
    return {WHITE_TILE:xscore, BLACK_TILE:oscore}

'''
def enterPlayerTile():
    # Draws the text and handles the mouse click events for letting
    # the player choose which color they want to be.  Returns
    # [WHITE_TILE, BLACK_TILE] if the player chooses to be White,
    # [BLACK_TILE, WHITE_TILE] if Black.

    # Create the text.
    textSurf = FONT.render('Do you want to be white(A) or black(B)?', True, TEXTCOLOR, TEXTBGCOLOR1)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

    xSurf = BIGFONT.render('White', True, TEXTCOLOR, TEXTBGCOLOR1)
    xRect = xSurf.get_rect()
    xRect.center = (int(WINDOWWIDTH / 2) - 60, int(WINDOWHEIGHT / 2) + 40)

    oSurf = BIGFONT.render('Black', True, TEXTCOLOR, TEXTBGCOLOR1)
    oRect = oSurf.get_rect()
    oRect.center = (int(WINDOWWIDTH / 2) + 60, int(WINDOWHEIGHT / 2) + 40)

    while True:
        # Keep looping until the player has clicked on a color.
        if buttons.checkKey ("A"):
           print ("A button detected" )
           return [WHITE_TILE, BLACK_TILE]
        if buttons.checkKey ("B"):
           print ("B button detected")          
           return [BLACK_TILE, WHITE_TILE]
           
        # Draw the screen.
        DISPLAYSURF.blit(textSurf, textRect)
        DISPLAYSURF.blit(xSurf, xRect)
        DISPLAYSURF.blit(oSurf, oRect)
        pygame.display.update()
        MAINCLOCK.tick(FPS)
'''

def makeMove(board, tile, xstart, ystart, realMove=False):
    # Place the tile on the board at xstart, ystart, and flip tiles
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile

    if realMove:
        animateTileChange(tilesToFlip, tile, (xstart, ystart))

    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or \
           (x == BOARDWIDTH and y == 0) or \
           (x == 0 and y == BOARDHEIGHT) or \
           (x == BOARDWIDTH and y == BOARDHEIGHT)


def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)

    # always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Go through all possible moves and remember the best scoring move
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = copy.deepcopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

if __name__ == '__main__':
    main()