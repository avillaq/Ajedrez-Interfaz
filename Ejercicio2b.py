from interpreter import draw
from chessPictures import *

col1 = knight.under(knight.negative().verticalMirror())
col2 = knight.negative().under(knight.verticalMirror())

draw(col1.join(col2))