from django.test import TestCase
from roman import int_to_roman


class IntToRomanTestCase(TestCase):

    def test_errors_non_int(self):
        ##this tests to make sure a non int will raise an exception
        with self.assertRaises(Exception) as cm:
            int_to_roman('cow')
        self.assertTrue('Input value is not an interger' == cm.exception.message)

    def test_errors_non_int_float(self):
        ##this tests to make sure a non int will raise an exception
        with self.assertRaises(Exception) as cm:
            int_to_roman(3.0)
        self.assertTrue('Input value is not an interger' == cm.exception.message)

    def test_errors_greater_than_expected(self):
        ##tests to make sure nothing greater than 3999 will work
        with self.assertRaises(Exception) as cm:
            int_to_roman(5000)
        self.assertTrue('input is out of Range 1-3999' == cm.exception.message)

    def test_errors_less_than_expected(self):
        ##tests to make sure nothing less than 1 will work
        with self.assertRaises(Exception) as cm:
            int_to_roman(-10)
        self.assertTrue('input is out of Range 1-3999' == cm.exception.message)

    def test_test_cases_listed(self):
        self.assertEqual(int_to_roman(6), 'VI')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(18), 'XVIII')
        self.assertEqual(int_to_roman(19), 'XIX')
        self.assertEqual(int_to_roman(38), 'XXXVIII')
        self.assertEqual(int_to_roman(39), 'XXXIX')
        self.assertEqual(int_to_roman(40), 'XL')
        self.assertEqual(int_to_roman(98), 'XCVIII')
        self.assertEqual(int_to_roman(388), 'CCCLXXXVIII')
        self.assertEqual(int_to_roman(499), 'CDXCIX')
        self.assertEqual(int_to_roman(867), 'DCCCLXVII')
        self.assertEqual(int_to_roman(1998), 'MCMXCVIII')

        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')





