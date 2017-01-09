from superhero import *
from flying import *
from running import *
from swimming import *
from sidekick import *


class Superman(Superhero, Flying, Running, Swimming):

  def __init__(self):
    Superhero.__init__(self, "Superman")
    self.air_speed = 1000000
