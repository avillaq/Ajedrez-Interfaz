from interpreter import draw
from chessPictures import *

col1 = knight.negative().up(knight)
col2 = knight.up(knight.negative())

draw(col1.join(col2))