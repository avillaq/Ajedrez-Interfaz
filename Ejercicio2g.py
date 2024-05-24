from interpreter import draw
from chessPictures import *

##### Piezas Negras #####

# Torres
torreIzquierdo = rock.negative().ponerEnCasillero(0)
torreDerecho = rock.negative().ponerEnCasillero(1)

# Caballos
caballoIzquierdo = knight.negative().ponerEnCasillero(1)
caballoDerecho = knight.negative().ponerEnCasillero(0)

# Alfiles
alfilIzquierdo = bishop.negative().ponerEnCasillero(0)
alfilDerecho = bishop.negative().ponerEnCasillero(1)

# Reina y Rey 
reina = queen.negative().ponerEnCasillero(1)
rey = king.negative().ponerEnCasillero(0)

# Peones
peonIzquierdo = pawn.negative().ponerEnCasillero(1)
peonDerecho = pawn.negative().ponerEnCasillero(0)

# Fila Principal de la piezas negras
fila_principal_negras = torreIzquierdo.join(caballoIzquierdo).join(alfilIzquierdo).join(reina).join(rey).join(alfilDerecho).join(caballoDerecho).join(torreDerecho)

# Fila de peones de las piezas negras
fila_peones_negras = peonIzquierdo.join(peonDerecho)
draw(fila_peones_negras.horizontalRepeat(3))

