from route import Route

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
    