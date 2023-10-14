from time_ import Time
from stop import Stop

class Route:

  def __init__(self, t: Time, s1: Stop, s2: Stop) -> None:
    """
    creates a route to be taken by a person

    :param t: starting time for the route
    :param s1: first stop (beginning of the route)
    :param s2: last stop (end of the route)
    """
    self.start_time = t
    self.begin = s1
    self.end = s2