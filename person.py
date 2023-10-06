from route import Route

class Person:

  def __init__(self,g: Route, b: Route, n:str) -> None:
    self.go= g
    self.back = b
    self.name = n
    