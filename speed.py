from distance import Distance
from time_ import Time

class Speed:

  def __init__(self, *args) -> None:

    if len(args) == 1:
      try:
        self._value = float(args[0])
      except ValueError as err:
        print(str(type(args[0]).__name__) + " is not of type 'int'")
        raise TypeError() from err
    elif len(args) == 2:
      try:
        self._value = float(args[0].value / args[1].value)
      except ValueError as err:
        print("Incorrect type is not of type 'Distance' and 'Time'")
        raise TypeError() from err

  def __str__(self) -> str:
    return f"{type(self).__name__} value = {self._value}"

  @property
  def value(self) -> float:
    return self._value

  @value.setter
  def value(self, v: int):
    self._value = v

  def __add__(self, o):
    return self._value + o.value

  def __sub__(self, o):
    return self._value - o.value

  def __mul__(self, o):
    return self._value * o.value

  def __truediv__(self, o):
    return self._value / o.value

  def __lt__(self, o):
    return self._value < o

  def __gt__(self, o):
    return self._value > o

  def __le__(self, o):
    return self._value <= o

  def __ge__(self, o):
    return self._value >= o
