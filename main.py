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

  for stop in stops:
    stop.how_to_go_to_others(buses, stops)
    print(stop.path_to_others, "\n")

  for p in people:
    #print(p.go.begin, "\n")
    p.go_to_stop(p.go.begin)

  #while True:
  #for bus in buses:
  i=0
  while i<6:
    #buses[0].go_to_next_stop(stops)
    #buses[2].go_to_next_stop(stops)
    i+=1


if __name__ == "__main__":  # run the main function
  main()
