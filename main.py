from distance import Distance
from speed import Speed
from time_ import Time
from bus import Bus
from person import Person
from stop import Stop
from road import Road
from route import Route
from utility import *
from parser import *

def main():
  parser = Parser("conf.json", "person.txt")
  parser.parse_conf()
  parser.parse_people()
  print(buses[0].path[0])

  for stop in stops:
    stop.how_to_go_to_others(buses, stops)
    #print(stop.path_to_others, "\n")

  for p in people:
    #print(p.go.begin.name, p.go.end.name, "\n")
    p.go_to_stop(p.go.begin)

  for bus in buses:
    bus.go_to_next_stop()
    
if __name__ == "__main__":  # run the main function
  main()
