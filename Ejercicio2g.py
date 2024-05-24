from interpreter import draw
from chessPictures import *

### Piezas Negras

# Torres
torreIzquierdo = rock.negative().ponerEnCasillero(0)
torreDerecho = rock.negative().ponerEnCasillero(1)

# Caballo
caballoIzquierdo = knight.negative().ponerEnCasillero(1)
caballoDerecho = knight.negative().ponerEnCasillero(0)

# Alfil
alfilIzquierdo = bishop.negative().ponerEnCasillero(0)
alfilDerecho = bishop.negative().ponerEnCasillero(1)

# Reina y Rey 
reina = queen.negative().ponerEnCasillero(1)
rey = king.negative().ponerEnCasillero(0)

row = torreIzquierdo.join(caballoIzquierdo).join(alfilIzquierdo).join(reina).join(rey).join(alfilDerecho).join(caballoDerecho).join(torreDerecho)

draw(row)

