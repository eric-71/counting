"""
Counter
"""


def main():
    """
    Select three numbers.
    The first value is the starting number.
    The second value is when counting will end.
    The third value will determine how the courter gets from start to finish.
    eg. 2's, 2 4 6 8 10
    """
    default = 0
    default1 = 1

    print('Hello!')

    while True:
        num1 = input('Enter a start value (Default: 0): ')
        if num1 == '':
            num1 = default
            break
        try:
            num1 = int(num1)
            break
        except ValueError:
            print('Whoops! Bad value! Please enter a start number only.\n')

    while True:
        num2 = input('Enter an end value: ')
        if num2 == '':
            print('Oh no! You must provide an end value to proceed.\n')
            continue
        if num2 == '0':
            print('Oh no! You must provide an end value to proceed.\n')
            continue
        try:
            num2 = int(num2)
            break
        except ValueError:
            print('Oh no! You must provide an end value to proceed.\n')

    while True:
        num3 = input('Enter a step value (Default: 1): ')
        if num3 == '':
            num3 = default1
            break
        try:
            num3 = int(num3)
            break
        except ValueError:
            print('Whoops! Invalid value! Please enter a step value only.\n')

    num2 += num3
    print ('')
    print('The numbers are: ', end = "")
    for counter in range(num1, num2, num3):
        print(counter, end = " ")


if __name__ == '__main__':
    main()
