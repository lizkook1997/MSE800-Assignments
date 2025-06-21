import unittest
# This imports Python’s built-in unittest module to help test code automatically.
class TestStringMethods(unittest.TestCase):
#  We define a test class that inherits from unittest.TestCase. This is how we group related test functions together.
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
# This checks if the string 'foo' becomes 'FOO' after using .upper().
# Test will pass because 'foo'.upper() = 'FOO'.

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())     # True because all letters are uppercase
        self.assertFalse('Foo'.isupper())    # False because 'o' is lowercase
# Tests if strings are in uppercase:

# 'FOO'.isupper() should return True

# 'Foo'.isupper() should return False

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

# tests whether .split() breaks the string into words correctly.
# 'hello world'.split() returns ['hello', 'world']

        with self.assertRaises(TypeError):
            s.split(2)
# This checks that if we try to use a non-string as a separator (like 2), it should raise a TypeError.
# This test will also pass if the error is raised properly.

if __name__ == '__main__':
    unittest.main()

#  This tells Python to run all the test cases in the file if the script is executed directly.
# This activity demonstrates unit testing using Python's unittest module. It tests string methods including .upper(), .isupper(), and .split() to ensure they behave as expected. It also includes error handling with assertRaises() for invalid input cases.