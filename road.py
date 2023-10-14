from distance import Distance


class Road:

  def __init__(self, n: int, s, d: Distance) -> None:
    """
    creates an instance of road

    :param n: number identifying the road
    :param s: list of stops related to the road
    :param d: length of the road
    """
    self.number = n
    self.stops = s  # tuple
    self._distance = d

  @property
  def distance(self) -> Distance:
    return self._distance

  @distance.setter
  def distance(self, d: Distance):
    self._distance = d