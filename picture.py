from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    i = len(self.img)-1
    while i > -1:
      horizontal.append(self.img[i])
      i-=1
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative_img = []
    for i in self.img:
      row = ""
      for j in i:
        row+=self._invColor(j)
      negative_img.append(row)
    return Picture(negative_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joined = []
    n = len(p.img)
    for i in range(n):
      joined.append(self.img[i]+p.img[i])
    return Picture(joined)

  def up(self, p):
    above = []
    for i in p.img:
      above.append(i)
    for i in self.img:
      above.append(i)
    
    return Picture(above)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    below = []
    for i in self.img:
      below.append(i)

    for i in p.img:
      below.append(i)
    return Picture(below)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeat = []
    for j in self.img:
      row = ""
      for i in range(n+1):
        row+=j
      repeat.append(row)
    return Picture(repeat)

  def verticalRepeat(self, n):
    repeat = []
    for i in range(n+1):
      for j in self.img:
        repeat.append(j)

    return Picture(repeat)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotated = [""]*(len(self.img))
    for i in self.img:
      n = len(rotated)
      for char in i:
        rotated[n-1]+=char
        n-=1

    return Picture(rotated)

