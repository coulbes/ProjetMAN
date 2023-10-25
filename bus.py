from distance import Distance
from speed import Speed
from time_ import Time
from utility import get_stop_by_name

class Bus:

  #remember: rewrite Python language
  def __init__(self, load_capacity: int, loading_speed: Time, unloading_speed: Time, speed: Speed, path) -> None:
    self.load = []
    self.capacity = load_capacity
    self.loading_speed = loading_speed
    self.unloading_speed = unloading_speed
    self.speed = speed
    self.path = path # list of stops name

  def __str__(self) -> str:
    return f"{type(self).__name__}"

  def add_person(self, person):
    self.load.append(person)

  def pop_person(self):
    self.load.pop()

  def go_to_next_stop(self, stops):
    for stop_name in self.path:
      stop = get_stop_by_name(stops, stop_name)
      self.manage_load(stop)

  def manage_load(self, stop):
    # if the bus is not full and stop queue isn't empty, add the person to the queue
    while len(self.load) < self.capacity and len(stop.queue) != 0:  
      stop.add_person_to_bus(self)
      # print(f"{self.load[-1].name} added to the bus {self.path}")