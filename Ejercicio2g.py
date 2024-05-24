from interpreter import draw
from chessPictures import *

##### Piezas Negras #####

# Torres
torreIzquierdo = square.under(rock.negative())
torreDerecho = square.negative().under(rock.negative())

# Caballos
caballoIzquierdo = square.negative().under(knight.negative())
caballoDerecho = square.under(knight.negative())

# Alfiles
alfilIzquierdo = square.under(bishop.negative())
alfilDerecho = square.negative().under(bishop.negative())

# Reina y Rey 
reina = square.negative().under(queen.negative())
rey = square.under(king.negative())

# Peones
peonIzquierdo = square.negative().under(pawn.negative())
peonDerecho = square.under(pawn.negative())

# Fila Principal de la piezas negras
fila_principal_negras = torreIzquierdo.join(caballoIzquierdo).join(alfilIzquierdo).join(reina).join(rey).join(alfilDerecho).join(caballoDerecho).join(torreDerecho)

# Fila de peones de las piezas negras
fila_peones_negras = peonIzquierdo.join(peonDerecho).horizontalRepeat(3)

##### Piezas Blancas #####

# Fila Principal de la piezas blancas
fila_principal_blancas = fila_principal_negras.negative()

# Fila de peones de las piezas blancas
fila_peones_blancas = fila_peones_negras.negative()

draw(fila_principal_blancas.up(fila_peones_blancas))

