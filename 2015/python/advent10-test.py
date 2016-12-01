import unittest
import advent10 as a

class TestLookAndSay(unittest.TestCase):

    def test_1(self):
        self.assertEqual(a.look_and_say('1'), '11')

    def test_11(self):
        self.assertEqual(a.look_and_say('11'), '21')

    def test_21(self):
        self.assertEqual(a.look_and_say('21'), '1211')

    def test_1211(self):
        self.assertEqual(a.look_and_say('1211'), '111221')

    def test_111221(self):
        expected = '312211'
        actual = a.look_and_say('111221')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
