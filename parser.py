import json
from bus import Bus
from stop import Stop
from road import Road
from speed import Speed
from time_ import Time
from distance import Distance
from person import Person


class Parser:

  def __init__(self, fn1: str, fn2: str) -> None:
    self.filename_conf = fn1
    self.filename_people = fn2
    self.buses = []
    self.stops = []
    self.roads = []
    self.people = []

  def parse_people(self):
    with open(self.filename_people, 'r') as file:
      for line in file:
        for i in line[0]:
          self.people.append(Person())
        

  def parse_conf(self):
    parsed_json = ""
    with open(self.filename_conf, 'r') as file:
      parsed_json = json.loads(file.read())
    self.parse_stops(parsed_json)
    self.parse_roads(parsed_json)
    self.parse_buses(parsed_json)

  def parse_stops(self, dict):
    for stop in dict["stops"]:
      self.stops.append(Stop(stop["roads_linked"], 0))

  def parse_roads(self, dict):
    for road in dict["roads"]:
      self.roads.append(
          Road((road["stops"][0], road["stops"][1]),
               Distance(int(road["distance"]))))

  def parse_buses(self, dict):
    speed = []
    s1 = 0
    s2 = 0
    for bus in dict["buses"]:
      speed = bus["speed"].split("/")
      s1 = int(speed[0])
      s2 = int(speed[1])
      self.buses.append(
          Bus(bus["capacity"], Time(bus["loading_speed"]),
              Speed(Distance(s1), Time(s2)), bus["loop"]))
