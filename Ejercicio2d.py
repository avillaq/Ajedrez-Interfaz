from interpreter import draw
from chessPictures import *

casillero1 = square
casillero2 = square.negative()

union = casillero1.join(casillero2)

draw(union.horizontalRepeat(3))