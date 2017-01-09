class Flight(object):

  def __init__(self):
    self.air_speed = 0
    self.max_load = 0
    self.max_altitude = 0

  def fly(self):
    print("I am flying at {} m/s".format(self.air_speed))


class Running(object):

  def __init__(self):
    self.ground_speed = 0
    self.acceleration_rate = 0

  def run(self):
    pass


class Swimming(object):

  def __init__(self):
    self.swim_speed = 0
    self.max_depth = 0

  def swim(self):
    pass


class Sidekick():

    def __init__(self, name):
      self.name = name
      self.gender = ""
      self.alter_ego_profession = None

    def __str__(self):
      return self.name

class Superhero(object):

    def __init__(self, name):
      self.powers = set()
      self.name = name
      self.gender = ""
      self.super_friends = set()
      self.evil_enemies = set()
      self.sidekicks = set()
      self.weaknesses = set()
      self.lair = ""
      self.biological_parents = tuple()

    def fight(self):
      pass

    def get_powers(self):
      return self.powers

    def add_power(self, new_power):
      self.powers.add(new_power)

    def remove_power(self, power_to_remove):
      self.powers.remove(power_to_remove)

    def __str__(self):
      power_output = ""

      for power in self.get_powers():
        power_output += power + ","

      return "{} the superhero with the powers: {}".format(self.name, power_output[0:-1])


class Superman(Superhero, Flight, Running, Swimming):

  def __init__(self):
    Superhero.__init__(self, "Superman")
    self.air_speed = 1000000


jimmy_olsen = Sidekick("Jimmy Olsen")

superman = Superman()
superman.sidekicks.add(jimmy_olsen)

superman.add_power("X-Ray Vision")
superman.fly()

print(superman.sidekicks)


