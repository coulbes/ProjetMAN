from distance import Distance
from speed import Speed
from time_ import Time

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

  def go_to_next_stop(self):
    for i in range(len(self.path)):
      self.manage_load(self.path[i])

  def manage_load(self, stop_name):
    pass
    # if the bus is not full, add the person to the queue
    # if len(self.load) < self.capacity and len(stop.queue) != 0:
     # self.load.append(stop.queue.pop(0))