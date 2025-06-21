

import unittest  # Importing Python's built-in unit testing framework

# Creating a test class for string-related test cases
class TestStringMethods(unittest.TestCase):

    # Test 1: Checks if 'foo'.upper() correctly returns 'FOO'
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')  # Expected output: 'FOO'

    # Test 2: Checks if isupper() works correctly
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())       # Should return True
        self.assertFalse('Foo'.isupper())      # Should return False because 'o' is lowercase

    # Test 3: Checks if split() breaks the string correctly
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])  # Expected list after splitting
        # This checks that using a non-string separator raises a TypeError
        with self.assertRaises(TypeError):
            s.split(2)

    # Test 4: New test case – checks if '123'.isdigit() returns True
    def test_isdigit(self):
        self.assertTrue('123'.isdigit())  # Should return True because all characters are digits

# This runs all the test cases when the script is executed directly
if __name__ == '__main__':
    unittest.main()
