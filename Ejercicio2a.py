from interpreter import draw
from chessPictures import *

col1 = knight.under(knight.negative())
col2 = knight.negative().under(knight)

draw(col1.join(col2))