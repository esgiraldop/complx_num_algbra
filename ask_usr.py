''' Tasks to do:
    - Check nothing other than digits are entered by the user
    - Check input is of the form "n + mi", where "n" is the real part and "m" the complex part
    - The user should be able to enter fractions or decimals and get the answer in both formats
    - Format the input so there are not whitespaces between terms and/or numbers
    - Check there are only two signs: One for the real part and one for the complex part
    - Numbers with decimals and fractions combined are not avoided. For example: (3.345/3.545)
    - Check the user does not input special characters that are not "(", ")", "/", "+", "-", ".", "i" or numbers
    - If the user enters fractions, check that no signs are entered inside the parenthese like (-45/+56) but enters
        -(45/56)
    - Check the user always enter fractions inside parentheses.
    - If user entered the two terms, check the second term has an "i" at the end. If it does not, add the 'i' to the
        second term
    - The user cannot enter such a thing as "-(5/3)++(67/6)i" '''

import re
import calculator as calc

def exceeds_max_spcial_chars(num, allowd_spcial_chars_list, allowd_spcial_chars_num):
    for char, max_coincdnses in zip(allowd_spcial_chars_list, allowd_spcial_chars_num):
        coincdnses = len(re.findall(char, num))
        if coincdnses > max_coincdnses:
            print("Incorrect format. Please try again.")
            return True

    return False

def is_input_wrong(num):
    '''
        Function created for easy testing with unit testing
    :param num:
    :return:
    '''
    allowd_spcial_chars = r'\(|\)|\/|\.|\+|\-|i|\d'
    not_allowd_spcial_chars = r'[^\(|\)|\/|\.|\+|\-|i\d]'
    allowd_spcial_chars_list = [r"\(", r"\)", r"\/", r"\.", r"\+", r"\-", r"i"]
    allowd_spcial_chars_num = [2, 2, 2, 2, 2, 2, 1]

    if ' ' in num:
        print("Whitespaces are not allowed.")
        return True

    if re.match(not_allowd_spcial_chars, num) != None:
        print("Please recall the only accepted characters are '(', ')', '/', '+', '-', '.', 'i' ")
        return True

    # Checking the maximum number of special characters
    if exceeds_max_spcial_chars(num, allowd_spcial_chars_list, allowd_spcial_chars_num):
        return True

    if len(re.findall('\+|\-', num)) > 2:
        print('Incorrect format. Please try again')
        return True

    num_open_paren = len(re.findall('\(', num))
    num_close_paren = len(re.findall('\)', num))
    if num_open_paren != num_close_paren:
        print('Incorrect format. Please try again')
        return True

    # If all the previous checks fail (Meaning no conditional succeeds), the input is ok and the outer while loop is
        # ended
    return False

def ask_num():
    next_loop = True

    while next_loop:
        num = input('Please enter a number: ')
        next_loop = is_input_wrong(num)

    return num


if __name__ == '__main__':
    num = ask_num()
    print('Your complex number is: ', num)