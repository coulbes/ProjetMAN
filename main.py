from distance import Distance
from speed import Speed
from time_ import Time
from bus import Bus
from person import Person
from stop import Stop
from road import Road
from route import Route
from parser import Parser



parser = Parser("conf.json", "person.txt")
parser.parse_conf()
parser.parse_people()