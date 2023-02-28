#!/usr/bin/env python3
'''
Unit test for calc.py
'''

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        """Test the add function"""
        self.assertEqual(calc.add(12, 4), 16)
        self.assertEqual(calc.add(1, -3), -2)
        self.assertEqual(calc.add(-1, -3), -4)

    def test_subtract(self):
        """Test the subtract function"""
        self.assertEqual(calc.subtract(12, 4), 8)
        self.assertEqual(calc.subtract(1, -3), 4)
        self.assertEqual(calc.subtract(-1, -3), 2)

    def test_multiply(self):
        """Test the add function"""
        self.assertEqual(calc.multiply(12, 4), 48)
        self.assertEqual(calc.multiply(1, -3), -3)
        self.assertEqual(calc.multiply(-1, -3), 3)
    
    def test_divide(self):
        """Test the add function"""
        self.assertEqual(calc.divide(12, 4), 3)
        self.assertEqual(calc.divide(0, 4), 0)
        self.assertEqual(calc.divide(5, 2), 2.5)

        #self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()