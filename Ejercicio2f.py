from interpreter import draw
from chessPictures import *

fila1 = square.join(square.negative()).horizontalRepeat(3)
fila2 = fila1.negative()

union = fila2.up(fila1)

draw(union.verticalRepeat(1))