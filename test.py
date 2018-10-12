from calcul_salaire import *
class MyFirstTests(unittest.TestCase):
    def test_person1(self):
        self.assertEqual(calcul_salaire(metier, experience), '4000')

    def test_person2(self):
       self.assertEqual(calcul_salaire(metier, experience), '7000')

    def test_person3(self):
        self.assertEqual(calcul_salaire(metier, experience), '5000')

   
