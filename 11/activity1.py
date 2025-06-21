# Importing the unittest module to perform unit testing in Python
import unittest

# A simple function that returns the sum of two numbers
def add(x, y):
    return x + y

# Creating a test class that inherits from unittest.TestCase
# This class will contain test methods to verify if the add() function works correctly
class TestAdd(unittest.TestCase):

    # This method will run tests on the add() function
    def test_add(self):
        # Testing if 2 + 3 equals 5
        self.assertEqual(add(2, 3), 5)
        
        # Testing if -1 + 1 equals 0
        self.assertEqual(add(-1, 1), 0)
        
        # Testing if 0 + 0 equals 0
        self.assertEqual(add(0, 0), 0)

# This block ensures that the tests will run when the script is executed
if __name__ == "__main__":
    unittest.main()
