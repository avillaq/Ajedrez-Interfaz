from interpreter import draw
from chessPictures import *

### Piezas Negras

# Torres
torreIzquierdo = rock.negative().ponerEnCasillero(0)
torreDerecho = rock.negative().ponerEnCasillero(1)

# Caballo
caballoIzquierdo = knight.negative().ponerEnCasillero(1)
caballoDerecho = knight.negative().ponerEnCasillero(0)



draw(caballoIzquierdo)

