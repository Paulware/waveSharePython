#!/bin/sh
# Thanks to KenT for contributions

RET=0
while [ $RET -eq 0 ]; do
  GAME=$(zenity --width=350 --height=700 --list \
    --title="Choose the Python game to launch" \
    --text="Games by Al Sweigart. Manual at inventwithpython.com/pygame" \
    --column="Script name" --column="Description" \
    flippy "A game like reversi" \
    fourinarow "Get four in a row" \
    gemgem "A tile matching puzzle" \
    inkspill "Flood the screen with pixels" \
    memorypuzzle "Test your memory" \
    pentomino "5 block Tetris" \
    simulate "Repeat the pattern" \
    slidepuzzle "Traditional slide puzzle" \
    squirrel "Eat the smaller squirrels" \
    starpusher "Sokoban" \
    tetromino "Tetris-like game" \
    tetrominoforidiots "Tetris for Idiots" \
    wormy "Snake-like game" \
    website "inventwithpython.com")
  RET=$?
  echo $RET
  if [ "$RET" -eq 0 ]
  then
     if [ "$GAME" = "website" ]
     then
        sensible-browser "http://inventwithpython.com/pygame"
     else
       if [ "$GAME" != "" ]; then
          cd /usr/share/python_games
          python $GAME.py
       fi
     fi
  fi
done
