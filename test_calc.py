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

    def test_subtract(self):
        """Test the subtract function"""
        self.assertEquals(calc.subtract(12, 4), 8)
        self.assertEquals(calc.subtract(1, -3), 4)
        self.assertEquals(calc.subtract(-1, -3), 2)

    def test_multiply(self):
        """Test the add function"""
        self.assertEquals(calc.multiply(12, 4), 48)
        self.assertEquals(calc.multiply(1, -3), -3)
        self.assertEquals(calc.multiply(-1, -3), 3)
    
    def test_divide(self):
        """Test the add function"""
        self.assertEquals(calc.divide(12, 4), 3)
        self.assertEquals(calc.divide(0, 4), 0)
        self.assertEquals(calc.divide(5, 2), 2.5)

        #self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()