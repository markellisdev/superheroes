from superman import *

jimmy_olsen = Sidekick("Jimmy Olsen")

superman = Superman()
superman.sidekicks.add(jimmy_olsen)

superman.add_power("X-Ray Vision")
superman.fly()

print(superman.sidekicks)