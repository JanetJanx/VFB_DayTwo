import unittest
from app.vowel_duplicates import vowels

class VowelTest (unittest.TestCase):
    
    def test_vowels(self):
        self.assertEqual(vowels("janet"), ('ae', 0))
        self.assertEqual(vowels("urbanisation"), ('aiou', 3))
        self.assertEqual(vowels("ur,*sati!on"), ('aiou', 0))


if __name__== '__main__':
    unittest.main()
