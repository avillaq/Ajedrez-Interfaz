from interpreter import draw
from chessPictures import *

col1 = knight.negative().verticalMirror().up(knight)
col2 = knight.verticalMirror().up(knight.negative())

draw(col1.join(col2))