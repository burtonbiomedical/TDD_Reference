import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        #This first test will test the emails
        print('test_email')
        #Create two employees
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        #Test that we create their email correctly
        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')
        #Change the employees names
        emp_1.first = 'John'
        emp_2.first = 'Jane'
        #Test that the emails have changed accordingly
        self.assertEqual(emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        #Same as above but with the full name instead
        print('test_fullname')
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        #Create two employees, then apply a raise and test
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        print('test_apply_raise')
        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)

#The problem with the above code is that for each test we are creating new employees
#This repeated code is not just inefficient, but could be problematic if we need to change
#our input in the future, as we would need to go into every test and change the employee definitions

#In the class below, we use the setup and tear down methods

class TestEmployee_classMethod(unittest.TestCase):

    #Setup and tear down class runs once before and after ALL tests respectively
    #The classmethod decorator means this is running a class rather than just an instance of
    #a class. These can be useful if you want to do something just once e.g. populate a database
    #before running all your tests
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    #Must be cammel case. setUp method is run before every single test
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    #Must be cammel case. tearDown method is run after every single test
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()
