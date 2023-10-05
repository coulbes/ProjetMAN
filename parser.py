import json

class Parser:

  def __init__(self, fn:str) -> None:
    self.filename = fn
    self.buses = []
    self.stops = []
    self.roads = []
    self.people = []

  def parse(self):
    with open(self.filename, 'r')as file:
      for category in file:
        