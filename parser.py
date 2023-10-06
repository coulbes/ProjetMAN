import json
from bus import Bus
from stop import Stop
from road import Road
from route import Route
from speed import Speed
from time_ import Time
from distance import Distance
from person import Person

global buses
global stops
global roads
global people

buses = []
stops = []
roads = []
people = []
class Parser:

  def __init__(self, fn1: str, fn2: str) -> None:
    self.filename_conf = fn1
    self.filename_people = fn2

  def parse_people(self):
    splited = []
    s1: Stop
    s2: Stop
    s3: Stop
    s4: Stop
    with open(self.filename_people, 'r') as file:
      for line in file:
        splited = line.split(" ")
        for e in stops:
          if e.name == splited[3][0]:
            s1 = e
          if e.name == splited[3][1]:
            s2 = e
          if e.name == splited[5][0]:
            s3 = e
          if e.name == splited[5][1]:
            s4 = e

        try:
          for i in range(int(splited[0])):
            people.append(
                Person(Route(Time(int(splited[2])), s1, s2),
                       Route(Time(int(splited[4])), s3, s4),
                       splited[1] + str(i)))
        except UnboundLocalError as err:
          raise ValueError("Invalid stop name") from err
        except TypeError as err:
          raise TypeError("Time is not of type 'int'") from err

  def parse_conf(self):
    parsed_json = ""
    with open(self.filename_conf, 'r') as file:
      parsed_json = json.loads(file.read())
    self.parse_stops(parsed_json)
    self.parse_roads(parsed_json)
    self.parse_buses(parsed_json)

  def parse_stops(self, dict):
    for stop in dict["stops"]:
      stops.append(Stop(stop["roads_linked"], [], stop["name"]))

  def parse_roads(self, dict):
    for road in dict["roads"]:
      roads.append(
          Road(int(road["number"]), (road["stops"][0], road["stops"][1]),
               Distance(int(road["distance"]))))

  def parse_buses(self, dict):
    speed = []
    s1 = 0
    s2 = 0
    for bus in dict["buses"]:
      speed = bus["speed"].split("/")
      s1 = int(speed[0])
      s2 = int(speed[1])
      buses.append(
          Bus(bus["capacity"], Time(bus["loading_speed"]),
              Speed(Distance(s1), Time(s2)), bus["loop"]))
