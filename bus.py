from distance import Distance
from speed import Speed
from time_ import Time

class Bus:

  #remember: rewrite Python language
  def __init__(self, load: int, loading_speed: Time, speed: Speed, path) -> None:
    self.load = int(load)
    self.loading_speed = loading_speed
    self.speed = speed
    self.path = path # list of stops

  def __str__(self) -> str:
    return f"{type(self).__name__}"