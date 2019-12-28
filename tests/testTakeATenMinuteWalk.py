import unittest
from take_a_ten_minute_walk import is_valid_walk


class TestTenMenuteWalk(unittest.TestCase):

    def testIsTenMinute(self):
        with self.subTest(i=1):
            self.assertTrue(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
        with self.subTest(i=2):
            self.assertTrue(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))

    def testIsNotTenMinute(self):
        with self.subTest(i=1):
            self.assertFalse(is_valid_walk(['s','n','s','n','s','n','s','n','s']) )
        with self.subTest(i=2):
            self.assertFalse(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
        with self.subTest(i=3):
            self.assertFalse(is_valid_walk(['n',]))
        with self.subTest(i=4):
            self.assertFalse(is_valid_walk([]))
        with self.subTest(i=5):
            self.assertFalse(is_valid_walk(['e','w','n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))

    def testShouldRetutnToStartPoint(self):
        with self.subTest(i=1):
            self.assertTrue(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
        with self.subTest(i=2):
            self.assertTrue(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))

    def testShouldNotRetutnToStartPoint(self):
        with self.subTest(i=1):
            self.assertFalse(is_valid_walk(['n','w','w','s','n','e','n','s','n','s']))
        with self.subTest(i=2):
            self.assertFalse(is_valid_walk(['w', 'w', 'w', 'e', 'n', 'e', 'w', 'e', 'w', 'e']))



if __name__ == '__main__':
    unittest.main()