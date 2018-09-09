import unittest
from vowel_duplicates import vowels

class VowelTest (unittest.TestCase):
    
    def test_vowels(self):
        self.assertEqual(vowels("janet"), ('ae', 0))
        self.assertEqual(vowels("urbanisation"), ('uaio', 3))
        self.assertEqual(vowels("ur,*sati!on"), ('uaio', 0))


if __name__== '__main__':
    unittest.main()
