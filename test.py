import unittest
import TenTimes

class TestMath(unittest.TestCase):
    def test(self):
        self.assertEqual(TenTimes.cps6410(7), 70)
  
if __name__ == '__main__':
    unittest.main()
