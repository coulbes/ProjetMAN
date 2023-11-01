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
    
  def pop_queue(self):
    self.queue.pop()

  def get_stop_by_name(self, stops, name):
    for stop in stops:
      if stop.name == name:
        return stop
        
  def manage_load(self, bus):
    for i in range(bus.capacity):
      for person in bus.load:
        if person.go.end.name == self.name:
          print(f"{person.name} get off the bus {bus.name}")
          self.queue.append(person)
          if person.back is not None:
            person.go = person.back
            person.back = None
          bus.load.remove(person)
          break
          
      if len(bus.load) < bus.capacity:
        for person in self.queue:
          if self.path_to_others.get(person.go.end.name) == bus:
            print(f"{person.name} added to the bus {bus.name}")
            bus.add_person(person)
            self.queue.remove(person)
            break

  def how_to_go_to_others(self, buses, stops):
    # Étape 1 : Trouver les bus directs vers d'autres arrêts
    for stop in stops:
        if self.name != stop.name:
            direct_bus = self.find_direct_bus(buses, stop)
            if direct_bus:
                self.path_to_others[stop.name] = direct_bus

    # Étape 2 : Examiner les arrêts sans itinéraire direct
    for stop in stops:
        if self.name != stop.name and stop.name not in self.path_to_others:
            # Pour chaque arrêt sans itinéraire direct
            for bus in buses:
              for stop_bus in bus.path:
                direct_bus_2 = self.find_direct_bus(buses, get_stop_by_name(stops, stop_bus))
                if direct_bus_2:
                  alternate_buses = (bus, stop_bus)
                  #alternate_buses.add(bus.name)
                  #alternate_buses.add(stop_bus)
                  #alternate_buses.add(direct_bus_2.name)
            if alternate_buses:
                self.path_to_others[stop.name] = alternate_buses

  def find_direct_bus(self, buses, stop):
    if(self.path_to_others.get(stop.name)):
      speed = self.path_to_others.get(stop.name).speed
    else:
      speed = 0
    for bus in buses:
        if self.name in bus.path and stop.name in bus.path and bus.speed > speed :
            return bus
    return None
      