''' Tasks to do:
    - Check nothing other than digits are entered by the user
    - Check input is of the form "n + mi", where "n" is the real part and "m" the complex part
    - The user should be able to enter fractions or decimals and get the answer in both formats
    - Check there are only two signs: One for the real part and one for the complex part
    - Numbers with decimals and fractions combined are not avoided. For example: (3.345/3.545)
    - Check the user does not input special characters that are not "(", ")", "/", "+", "-", ".", "i" or numbers
    - If the user enters fractions, check that no signs are entered inside the parenthese like (-45/+56) but enters
        -(45/56)
    - Check the user always enter fractions inside parentheses.
    - If user entered the two terms, check the second term has an "i" at the end. If it does not, add the 'i' to the
        second term'''

import re
import calculator as calc

def exceeds_max_spcial_chars(num, allowd_spcial_chars_list, allowd_spcial_chars_num):
    for char, max_coincdnses in zip(allowd_spcial_chars_list, allowd_spcial_chars_num):
        coincdnses = len(re.findall(char, num))
        if coincdnses > max_coincdnses:
            print("Incorrect format. Please try again.")
            return True

    return False

def not_closed_parentheses(num):
    num_open_paren = len(re.findall(r'\(', num))
    num_close_paren = len(re.findall(r'\)', num))
    if num_open_paren != num_close_paren:
        print('Incorrect format. Please try again')
        return True

def is_input_wrong(num):
    '''
        Function to check the input given by the user is in the correct format
        The program checks in order if:
            1. There are not whitespaces
            2. Only numbers or these special characters are entered: "(", ")", "/", "+", "-", ".", "i"
            3. The special characters are entered a maximum number of times
            4. '+' and/or '-' are not entered one next to the other
            5. There is a closing ')' parenthesis for every opening parenthesis '('
            6. A special character does not follow another special character.
                The special characters are: "(", ")", "/" and "."
                This helps checking for inputs like "(5/6)(5/8)i", "(5//6)(5/8)i", "3..4+i" or the like.
            7. The complex number is separable in a real and a complex part. Function real_complx_sepration() also
                helps checking if any of the numbers within a fractional is decimal, which is not allowed.
            8. After obtaining the real and complex part, no "i" is found in neither of the two
            9. The real part has maximum 1 especial character out of "(", ")", "/", "+", "-" or "."
            10. The complex part has only 1 especial character out of "(", ")", "/", "+", "-" or "."
            11. Checks #5 for the real part only
            12. Checks #5 for the complex part only
        This function was created for easy testing with unit testing
    :param num:
    :return: Boolean. True if there is an error in the input, False otherwise.
    '''
    allowd_spcial_chars = r'\(|\)|\/|\.|\+|\-|i|\d'
    not_allowd_spcial_chars = r'[^()i\/.+\-0-9]'
    allowd_spcial_chars_list = [r"\(", r"\)", r"\/", r"\.", r"\+|\-", r"i"]
    allowd_spcial_chars_num = [2, 2, 2, 2, 2, 1]

    if ' ' in num:
        print("Whitespaces are not allowed.")
        return True

    if len(re.findall(not_allowd_spcial_chars, num)) > 0:
        print("Please recall the only accepted characters are '(', ')', '/', '+', '-', '.', 'i' ")
        return True

    # Checking the maximum number of special characters
    if exceeds_max_spcial_chars(num, allowd_spcial_chars_list, allowd_spcial_chars_num):
        return True

    if len(re.findall(r'(?:\+|\-){2,}', num)) > 0: # For patterns like 1--5i or ++1-5i
        print('Incorrect format. Please try again')
        return True

    if not_closed_parentheses(num):
        return True

    chars = [r'\(', r'\)', r'\/', r'\.'] # Any of these characters cannot be next to the other
    for char1 in chars:
        for char2 in chars:
            pair = char1 + char2
            if re.findall(pair, num):
                print('Incorrect format. Please try again')
                return True

    try:
        real_prt, complx_prt = calc.real_complx_sepration(num)
    except:
        print('Incorrect format. Please try again')
        return True

    if 'i' in real_prt or 'i' in complx_prt:
        # If the input is correct, real_complx_sepration() should output two numbers without the "i". See script
            # "tests_real_complx_sepration.py"
        print('Incorrect format. Please try again')
        return True

    allowd_spcial_chars_num = [1, 1, 1, 1, 1, 0] # Applies for either "real_prt" or "complx_prt"
    if exceeds_max_spcial_chars(real_prt, allowd_spcial_chars_list, allowd_spcial_chars_num):
        return True

    if exceeds_max_spcial_chars(complx_prt, allowd_spcial_chars_list, allowd_spcial_chars_num):
        return True

    if not_closed_parentheses(real_prt):
        return True

    if not_closed_parentheses(complx_prt):
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