from interpreter import draw
from chessPictures import *

casillero1 = square.negative()
casillero2 = square

union = casillero1.join(casillero2)

draw(union.horizontalRepeat(3))