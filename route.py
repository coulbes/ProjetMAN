from time_ import Time
from stop import Stop

class Route:

  def __init__(self, t: Time, s1: Stop, s2: Stop) -> None:
    self.start_time = t
    self.begin = s1
    self.end = s2