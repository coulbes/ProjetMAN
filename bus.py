from distance import Distance
from speed import Speed
from time_ import Time
from utility import get_stop_by_name


class Bus:

  #remember: rewrite Python language
  def __init__(self, name, load_capacity: int, loading_speed: Time,
               unloading_speed: Time, speed: Speed, path) -> None:
    self.name = name
    self.load = []
    self.capacity = load_capacity
    self.loading_speed = loading_speed
    self.unloading_speed = unloading_speed
    self.speed = speed
    self.path = path  # list of stops name

  def __str__(self) -> str:
    return f"{type(self).__name__}"

  def add_person(self, person):
    self.load.append(person)

  def pop_person(self):
    self.load.pop()

  def go_to_next_stop(self, stops):
    for stop in stops:
      if self.path[0] == stop.name:
        next_stop = stop
        print("bus", self.name, "manage load for stop ", next_stop.name)
    next_stop.manage_load(self)
    self.path.append(self.path.pop(0))
