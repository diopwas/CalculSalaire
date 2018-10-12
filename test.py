import unittest
from calcul_salaire import *
class MyFirstTests(unittest.TestCase):
    def test_person1(self):
        self.assertEqual(calcul_salaire('Architecte', 4), '4000')

    def test_person2(self):
        self.assertEqual(calcul_salaire('Médecin', 8), '7000')

    def test_person3(self):
         self.assertEqual(calcul_salaire('consultant', 5), '5000')





