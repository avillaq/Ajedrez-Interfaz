from interpreter import draw
from chessPictures import *

fila1 = square.join(square.negative()).horizontalRepeat(3)
fila2 = fila1.negative()

union = fila1.under(fila2)

draw(union.verticalRepeat(1))