from distance import Distance


class Road:

  def __init__(self, n: int, s, d: Distance) -> None:
    self.number = n
    self.stops = s  # tuple
    self._distance = d

  @property
  def distance(self) -> Distance:
    return self._distance

  @distance.setter
  def distance(self, d: Distance):
    self._distance = d
