import unittest
from calculations.StatisticalCalculations import StatisticalCal

class TestStatisticalCalculations(unittest.TestCase):
    def test_average_input1(self):
        first_list = StatisticalCal([2,3,4,5,6])
        result1 = first_list.average_number()
        self.assertEqual(result1, 4)

    def test_average_input2(self):
        second_list = StatisticalCal([12,45,85,65])
        result2 = second_list.average_number()
        self.assertAlmostEqual(result2, 51.75)
    
    def test_median_input1(self):
        third_list = StatisticalCal([2,3,4,5,6])
        result3 = third_list.median_number()
        self.assertEqual(result3, 4)
    
    def test_median_input2(self):
        fourth_list = StatisticalCal([2,5,6,7,8])
        result4 = fourth_list.median_number()
        self.assertEqual(result4, 6) 


if __name__ == '__main__':
    unittest.main()
        