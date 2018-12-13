import unittest
from core import DXTR

class TestCore(unittest.TestCase):
    def setUp(self):
        self.dxtr = DXTR()

    def test_parse_command_string(self):
        self.assertEqual(self.dxtr.parse_command_string('test command'), 0)
        self.assertEqual(self.dxtr.parse_command_string(''), 1)

if __name__ == '__main__':
    unittest.main()
