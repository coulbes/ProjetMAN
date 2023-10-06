class Time:

  def __init__(self, v: int) -> None:
    try:
      self._value = int(v)
    except ValueError as err:
      raise TypeError(str(type(v).__name__) + " is not of type 'int'") from err

  def __str__(self) -> str:
    return f"{type(self).__name__} value = {self._value}"

  @property
  def value(self) -> int:
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
