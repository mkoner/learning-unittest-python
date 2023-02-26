#!/usr/bin/env python3
'''
Unit test for calc.py
'''

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        """Test the add function"""
        self.assertEquals(calc.add(12, 4), 16)
        self.assertEquals(calc.add(1, -3), -2)
        self.assertEquals(calc.add(-1, -3), -4)


if __name__ == '__main__':
    unittest.main()