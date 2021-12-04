#Nathan Gregorian Bailey
#Section 0003
#Program 13
#Created on December 4th 2021 
#Due December 10th 2021

import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):

        result = Grades.total([1,10,22])
        self.assertEqual(result,33,"The total function should return 33")

    def test_total_returns_0(self):

        result = Grades.total([])
        self.assertEqual(result,0,"the total function should return 0")
    
    def test_average_one(self):

        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result,5.33333,3,'the average function should return 5.33333')

    def test_average_two(self):

        result = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result,12.0000,4,'the average function should return 12.0000')

    def test_average_returns_nan(self):

        result = Grades.average([])
        self.assertIs(result,math.nan,'the average function should return math.nan')

    def test_median_odd_amount(self):

        result = Grades.median([2,5,1])
        self.assertEqual(result,2,'the median function should return 2')

    def test_median_even_amount(self):

        result = Grades.median([5,2,1,3])
        self.assertAlmostEqual(result,2.5,1,'the median function should return 2.5')

    def test_median_empty(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])
            self.assertEqual(result,[],'should raise an error')


unittest.main()