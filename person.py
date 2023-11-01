from route import Route
from stop import Stop

class Person:

  def __init__(self,g: Route, b: Route, n:str) -> None:
    """
    creates an instance of person

    :param g: the first itinerary of the person
    :param b: the second itinerary of the person
    :param n: the name of the person
    """
    self.go= g
    self.back = b
    self.name = n
    self.correspondance = None

  def go_to_stop(self, stop):
    stop.add_person(self)
    #print(len(stop.queue))
