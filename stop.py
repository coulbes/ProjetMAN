class Stop:

  def __init__(self, r, q, n: str) -> None:
    self.roads = r
    self.queue = q
    self.name = n
    #self.go_to_others = {}
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
        if (self.name != stop.name and self.name in bus.path and stop.name in bus.path):
          if (self.path_to_others.get(stop.name) is None):
            self.path_to_others[stop.name] = bus.path
          else:
            pass
          #  if (bus.speed < la speed du bus qui à le path présent dans self.path_to_others[stop.name]:
            
            #print("doublon :", self.name, "->", stop.name, ":", bus.path, " - ", self.path_to_others[stop.name])
            
    return(self.path_to_others)

    #return bus

  #ca c'est non
  #def add_path_to_others(self):
  #  self.path_to_others[self.name] = self.roads
  #  self.path_to_others[self.name].append(self.queue)
  #  print(self.path_to_others)
