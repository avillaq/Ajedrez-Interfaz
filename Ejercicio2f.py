from interpreter import draw
from chessPictures import *

fila1 = square.join(square.negative()).horizontalRepeat(3)
fila2 = fila1.negative()
draw(fila2)