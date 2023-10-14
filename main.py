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
    print(stop.name, stop.how_to_go_to_others(buses, stops), "\n")


if __name__ == "__main__":  # run the main function
  main()
