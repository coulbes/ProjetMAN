class Stop:

  def __init__(self, r, q, n: str) -> None:
    self.roads = r
    self.queue = q
    self.name = n
    self.path_to_others = {}  #take a list of buses

  def __str__(self) -> str:
    return f"{self.name}, {self.roads}, {self.queue}"

  

  def add_person(self, person):
    self.queue.append(person)

  def pop_queue(self):
    self.queue.pop()

  #creat a dict with the fastest bus.path to go to other stops 
  def how_to_go_to_others(self, buses, stops):
    for stop in stops:
      for bus in buses:
        #if we find both stops names in a bus path we add this bus to him path_to_others
        if (self.name != stop.name and self.name in bus.path and stop.name in bus.path):
          if (self.path_to_others.get(stop.name) is None or bus.speed > self.path_to_others[stop.name].speed):
            self.path_to_others[stop.name] = bus#.path
    return self.path_to_others
    