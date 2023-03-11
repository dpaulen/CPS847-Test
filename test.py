import unittest
import tentimes

class TestMath(unittest.TestCase):
    def test(self):
        self.assertEqual(tentimes.cps6410(7), 70)
  
if __name__ == '__main__':
    unittest.main()
