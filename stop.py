from os import name

from utility import get_stop_by_name


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

  def manage_load(self, bus):
    for i in range(bus.capacity):
      for person in self.queue:
        if self.path_to_others.get(person.go.end.name) == bus:
          print(f"{person.name} added to the bus {bus.path}")
          bus.add_person(person)
          self.queue.remove(person)
          break

      for person in bus.load:
        if person.go.end.name == self.name:
          print(
              f"{person.name} get off the bus {bus.path} at stop {self.name}")
          self.queue.append(person)
          bus.load.remove(person)
          break

  def add_person_to_bus(self, bus):
    tmp = []
    for person in self.queue:
      if self.path_to_others.get(
          person.go.end.name) == bus and len(bus.load) < bus.capacity:
        bus.add_person(person)
        print(f"{person.name} added to the bus {bus.path}")
      else:
        tmp.append(person)
    self.queue = tmp

  def get_person_off_bus(self, bus):
    for person in bus.load:
      if person.go.end.name == self.name:
        print(
            f"{bus.load.remove(person)} get off the bus {bus.path} at stop {self.name}"
        )
        self.queue.append(person)
        break

  def pop_queue(self):
    self.queue.pop()

  def get_stop_by_name(self, stops, name):
    for stop in stops:
      if stop.name == name:
        return stop

  def how_to_go_to_others(self, buses, stops):
    # Étape 1 : Trouver les bus directs vers d'autres arrêts
    for stop in stops:
        if self.name != stop.name:
            direct_bus = self.find_direct_bus(buses, stop)
            if direct_bus:
                self.path_to_others[stop.name] = direct_bus

    # Étape 2 : Examiner les arrêts sans itinéraire direct
    for stop in stops:
        while self.name != stop.name and stop.name not in self.path_to_others:
            # Pour chaque arrêt sans itinéraire direct
            alternate_buses = set()
            for bus in buses:
              for stop_bus in bus.path:
                direct_bus_2 = self.find_direct_bus(buses, get_stop_by_name(stops, stop_bus))
                if direct_bus_2:
                  alternate_buses.clear()
                  alternate_buses.add(bus)
                  alternate_buses.add(direct_bus_2)
            if alternate_buses:
                self.path_to_others[stop.name] = alternate_buses

  def find_direct_bus(self, buses, stop):
    for bus in buses:
        if self.name in bus.path and stop.name in bus.path:
            return bus
    return None
  
  #creat a dict with the fastest busesto take to go to other stops  
  def old_how_to_go_to_others(self,stop, buses, stops):
    for stop in stops:
      for bus in buses:
        if (self.name != stop.name and self.name in bus.path and stop.name in bus.path):
          #if we find both stops names in a bus path we add this bus to path_to_others
          if (self.path_to_others.get(stop.name) is None):
              self.path_to_others[stop.name] = bus
          elif (bus.speed > self.path_to_others[stop.name].speed):
            self.path_to_others[stop.name] = bus
            
            #for s in stops:
             # if s.name == stop.name:
              #  stop.how_to_go_to_others(self.path_to_others.values(), stops)
               # break
    
    #for stop in self.path_to_others:
      #print(stop)
      #if (self.path_to_others[stop] is None):
      #  print(stop)
      