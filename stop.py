class Stop:

  def __init__(self, r, q, n: str) -> None:
    self.name = n
    self.roads = r
    self.queue = q

  def __str__(self) -> str:
    return f"{self.name}, {self.roads}, {self.queue}"

  def add_person(self, person):
    self.queue.append(person)

  def pop_queue(self):
    self.queue.pop()