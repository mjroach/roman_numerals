import sys


def int_to_roman(value):
    #make sure the input is an int
    if type(value) != int:
        raise Exception('Input value is not an integer')

    #make sure nothing bad is passed to the function
    if value < 1 or value > 3999:
        raise Exception('input is out of Range 1-3999')

    results = ''
    roman_values = [(1000, 'M'),
                    (900, 'CM'),
                    (500, 'D'),
                    (400, 'CD'),
                    (100, 'C'),
                    (90, 'XC'),
                    (50, 'L'),
                    (40, 'XL'),
                    (10, 'X'),
                    (9, 'IX'),
                    (5, 'V'),
                    (4, 'IV'),
                    (1, 'I')]

    while value != 0:
        for int_value, numeral in roman_values:
            ##this must be a while case while checking intergershis case so that it will not create random letterings
            # for a while the test case 38 was returning  XIXVIXIII and not the proper results of XXXVIII
            while value >= int_value:
                results += numeral
                value -= int_value

    return results


if __name__ == '__main__':
    if sys.argv[1:]:

        for value in sys.argv[1:]:

            try:
                value_int = int(value)
            except ValueError:
                print('%s is not a valid int' % ( value,))
                value_int = None

            if value_int:
                value_roman = int_to_roman(value=value_int)
                print('%s converts to %s' % (value, value_roman))

    else:
        print('the first argument must be an integer, all other arguments will be ignored. ')