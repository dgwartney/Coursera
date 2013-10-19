# Unit testing framework
import unittest
import rpsls as r
import random
#
# Unit Tests
#
class TestRPSLS(unittest.TestCase):
    
    def setUp(self):
        """ (self) -> None

        Setup scaffolding for the tests
        """
        # Set a seed so our results are repeatable
        random.seed(1)

#
# Create our test cases using this mapping:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#
# Test cases for number_to_name()
#
    def test_number_to_name_0(self):
        self.assertEqual(r.number_to_name(0),'rock')
        
    def test_number_to_name_1(self):
        self.assertEqual(r.number_to_name(1),'Spock')
        
    def test_number_to_name_2(self):
        self.assertEqual(r.number_to_name(2),'paper')
        
    def test_number_to_name_3(self):
        self.assertEqual(r.number_to_name(3),'lizard')
        
    def test_number_to_name_4(self):
        self.assertEqual(r.number_to_name(4),'scissors')

    def test_number_to_name_100(self):
        self.assertEqual(r.number_to_name(100),'unknown')
        
    def test_number_to_name_negative1(self):
        self.assertEqual(r.number_to_name(-1),'unknown')


#
# Test cases for name_to_number()
#
    def test_name_to_number_rock(self):
        self.assertEqual(r.name_to_number('rock'),0)

    def test_name_to_number_Spock(self):
        self.assertEqual(r.name_to_number('Spock'),1)

    def test_name_to_number_paper(self):
        self.assertEqual(r.name_to_number('paper'),2)

    def test_name_to_number_lizard(self):
        self.assertEqual(r.name_to_number('lizard'),3)

    def test_name_to_number_scissors(self):
        self.assertEqual(r.name_to_number('scissors'),4)

    def test_name_to_number_thumb(self):
        self.assertEqual(r.name_to_number('thumb'),9999)
        
    def test_name_to_number_hand(self):
        self.assertEqual(r.name_to_number('hand'),9999)



# Computer numbers when seed is set to 1: 3, 0, 1, 3, 0

#
# Requires that we redirect standard out, unable to find a quick solution so manually test
#
##    def test_rpsls_rock(self):
##        result = "Player chooses rock\nComputer chooses lizard\nComputer wins1"
##        self.assertEqual(rpsls("rock"),result)
##        
##    def test_rpsls_rock(self):
##        result = "Player chooses Spock\nComputer chooses rock\nComputer wins!"
##        self.assertEqual(rpsls("rock"),result)
        

def run_unit_tests():
    """ (None) -> None

    Runs the unit tests to validate code
    """
    unittest.main()
#
# Run our unit tests
#
run_unit_tests()


