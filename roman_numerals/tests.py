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
        #these are the test cases listed on the evernote page.
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


    def test_main_function(self):
        #random int testing validated by an online converter
        self.assertEqual(int_to_roman(1986), 'MCMLXXXVI')
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(3320), 'MMMCCCXX')

        self.assertEqual(int_to_roman(3320), 'MMMCCCXX')
        self.assertEqual(int_to_roman(2724), 'MMDCCXXIV')
        self.assertEqual(int_to_roman(3632), 'MMMDCXXXII')
        self.assertEqual(int_to_roman(1190), 'MCXC')

        self.assertEqual(int_to_roman(795), 'DCCXCV')
        self.assertEqual(int_to_roman(3815), 'MMMDCCCXV')
        self.assertEqual(int_to_roman(2177), 'MMCLXXVII')
        self.assertEqual(int_to_roman(603), 'DCIII')

        self.assertEqual(int_to_roman(495), 'CDXCV')
        self.assertEqual(int_to_roman(383), 'CCCLXXXIII')
        self.assertEqual(int_to_roman(287), 'CCLXXXVII')
        self.assertEqual(int_to_roman(2678), 'MMDCLXXVIII')

        self.assertEqual(int_to_roman(3044), 'MMMXLIV')
        self.assertEqual(int_to_roman(1115), 'MCXV')
        self.assertEqual(int_to_roman(2598), 'MMDXCVIII')
        self.assertEqual(int_to_roman(2358), 'MMCCCLVIII')


    def test_main_basics(self):
        ##testing the basics
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(10), 'X')
        self.assertEqual(int_to_roman(50), 'L')
        self.assertEqual(int_to_roman(100), 'C')
        self.assertEqual(int_to_roman(500), 'D')
        self.assertEqual(int_to_roman(600), 'DC')
        self.assertEqual(int_to_roman(1000), 'M')




