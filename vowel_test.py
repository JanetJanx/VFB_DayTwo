import unittest
from vowel_duplicates import vowels

class VowelTest (unittest.TestCase):
    
    def vowels_test(self):
        self.assertEqual(vowels("janet"), (['a','e'], 0))
        self.assertEqual(vowels("urbanisation"), (['u', 'a', 'i', 'o'], 3))
         self.assertEqual(vowels("ur,*sati!on"), (['u', 'a', 'i', 'o'], 0))


if __name__== '__main__':
    unittest.main()
