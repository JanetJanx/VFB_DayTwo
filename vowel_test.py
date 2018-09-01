import unittest
from vowel_duplicates import vowels

class VowelTest (unittest.TestCase):
    
    def vowels_test(self):
        self.assertEqual(vowels("janet"), (['a','e'], 0))

if __name__== '__main__':
    unittest.main()
