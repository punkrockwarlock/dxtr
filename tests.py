import unittest
from core import DXTR

class TestCore(unittest.TestCase):
    def setUp(self):
        self.dxtr = DXTR()

    def test_parse_command_string(self):
        self.assertEqual(self.dxtr.parse_command_string(''), 1)
        self.assertEqual(self.dxtr.parse_command_string('GET ryan dob'), 0)
        self.assertEqual(self.dxtr.parse_command_string('RETRIEVE ryan dob'), 1)
        self.assertEqual(self.dxtr.parse_command_string('PUT ryan dob'), 2)

if __name__ == '__main__':
    unittest.main()
