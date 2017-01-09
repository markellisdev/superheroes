import unittest
from superman import *

class TestSuperman(unittest.TestCase):

    def test_SupermanIsASuperhero(self):

      superman = Superman()
      self.assertIsInstance(superman, Superhero)

    def test_SupermanIsAFlyingSuperhero(self):

      superman = Superman()
      self.assertIsInstance(superman, Flying)

    def test_SupermanIsASwimmingSuperhero(self):

      superman = Superman()
      self.assertIsInstance(superman, Swimming)

    def test_SupermanIsARunningSuperhero(self):

      superman = Superman()
      self.assertIsInstance(superman, Running)

if __name__ == '__main__':
    unittest.main()