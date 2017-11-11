import unittest
import calc

class TestCalc(unittest.TestCase):
    #All tests must have the naming convention 'test_*'
    def test_add(self):
        #If the add function returns 15 then test will pass
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)
        #Try to be thorough with your tests, if you come across a problem
        #add it to your unit tests so you do  not keep revisiting the same bugs
        #For example, the above assertions do not account for floor division that
        #would not return the remainder. Lets add an assertion test that would catch this
        self.assertEqual(calc.divide(5,2),2.5)
        #You can user assertRaises to check that an error is being raised when it
        #is supposed to be (dividing 10 by 0 should give a ValueError)
        self.assertRaises(ValueError, calc.divide, 10, 0)
        #This could also be tested using a context manager like so
        with self.assertRaises(ValueError):
            calc.divide(10,0)

if __name__ == '__main__':
    unittest.main()
