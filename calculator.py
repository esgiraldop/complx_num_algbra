import re

def search_middle_sign(num):
    # pattern = r'\d*\.?\d*(\+|-)\d*\.?\d*i' # Old pattern

    # Best pattern so far. Supports a much wider range of formats
    pattern = r'(?:\+|-)?\(?\d*\.?\d*\/?(?:\d*\.?\d*)\)?(\+|-)(?:\+|-)?\(?\d*\.?\d*\/?(?:\d*\.?\d*)\)?i?'

    sign = re.search(pattern, num).groups()[0]
    return sign

def real_complx_sepration(num):
    '''
        Function to separate the real and imaginary part out of a complex number.
        Accepted formats
        - "i", "-i", "+i" --> where i is sqrt(-1)
        - "mi" --> where "m" can be an real number and i is sqrt(-1)
        - "n" --> where "m" can be a real number
        - "n+mi" --> where "n" and "m" can be real numbers and i is sqrt(-1)
        :param num:
        :return:
    '''
    # pattern1 = r'^(?:\+|-)?\d*\.?\d*i' # First patter
    pattern1 = r'^(?:\+|-)?\(?\d*\.?\d*\/?(?:\d*\.?\d*)\)?i' # Best pattern so far

    # pattern2 = r'(?:(?:\+|-)?\d*\.?\d*)$' # First patter
    # pattern2 = r'(?:\+|-)?\d*\.?\d*[^i]$' # Second pattern
    pattern2 = r'(?:\+|-)?\(?\d*\.?\d*\/?(?:\d*\.?\d*)\)?[^i]$' # Best pattern so far
    if re.search(pattern1, num) != None: # For the format "mi", where m is a real number
        if num[0] != '-' and num[0] != '+':
            complx_prt = '+' + num[:-1] # Up to -1 to avoid the "i"
        else:
            complx_prt = num[:-1]

        real_prt = '0'
    elif re.search(pattern2, num) != None: # For the format "m", where m is a real number
        if num[0] != '-' and num[0] != '+':
            real_prt = '+' + num
        else:
            real_prt = num
        complx_prt = '0'
    else:
        # pattern3 = r'((?:\+|-)?\d*\.?\d*)((?:\+|-)?\d*\.?\d*)i' # First pattern3. Do not work for only real numbers
        # pattern3 = r'((?:\+|-)?\d*\.?\d*)((?:\+|-)?\d*\.?\d*)i?' # Second pattern3. Do not work for fractionals
        # real_prt = re.search(pattern3, num).groups()[0]
        # complx_prt = re.search(pattern3, num).groups()[1]

        # I found a better way to make the pattern shorter
        # pattern3 =r'((?:\+|-)?\d+\.?\d*?)i?' # Third pattern3. Shorter version of the previous one
        pattern3 = r'((?:\+|-)?\(?\d+\.?\d*?\/?(?:\d+\.?\d*?)?\)?)i?' # Current best one. Also supports fractional numbers
        found_prts = re.findall(pattern3, num)
        real_prt = found_prts[0]
        if len(found_prts) > 1:
            complx_prt = found_prts[1]
        elif len(found_prts) == 1:
            if 'i' in num:
                # The code was not working for '4+i' for example and fixing the regex is too complicated
                complx_prt = search_middle_sign(num)

    if complx_prt == '-' or complx_prt == '+': # In case the user enters for example 1+i or 1-i or 34.56+i
        complx_prt = complx_prt + '1'

    if ('(' in real_prt and ')' in real_prt) or ('(' in complx_prt and ')' in complx_prt):
        # Seems weird, but is an easy way to bypass what is coming for division, since coming complex numbers come
            # formatted already from function join_uppr_lwr_terms()
        if real_prt[0] == '+':
            real_prt = real_prt[1:]

        if complx_prt[0] == '+':
            complx_prt = complx_prt[1:]

        return real_prt, complx_prt
    else:
        real_prt, complx_prt = str(format_floatnum(float(real_prt))), str(format_floatnum(float(complx_prt)))

    return real_prt, complx_prt

def is_fraction(num):
    '''
        Function for checking whether the number is a fraction or not
        :param:
            num: String
        :return:
            Boolean. True for fraction, False otherwise
    '''
    return True

def decimal_2_frac(num):
    ''' Function to transform from decimal to fraction. Integers are transformed as well. "1" --> "(1/1)"
        This function:
        1. Checks if there is a minus and saves it somewhere else
        2. Splits the number in the integer and decimal parts
        3. Transforms the decimal part into a fraction (Core of the function. It deserves to be in another function)
        4. Adds the integer part to the fraction (Include function real_complx_sum)
        :param:
            num: String with the num to transform to fractional
        :return:
            frac: String with the num transformed into fractional
    '''

    if is_fraction(num) == False:
        sign = search_middle_sign(num) # If I used num[0] to retrieve the sign, it would no work for cases like "1.54"

        if sign == '-' or sign == '+':
            num = num[0:1]
            if sign == '+':
                sign = ''

        partition = num.partition('.')
        integ = partition[0]
        decim = partition[2]
        decim_frac = f'({decim}/1'+'0'*len(decim)+')'
        int_frac = f'({integ}/1)'
        frac = sum_frac(int_frac, decim_frac)

        return sign+frac

    return num # If the number was entered as a fraction by the user, there is no need to transform it

def format_floatnum(num):
    '''
        Function for formatting numbers. If there is a number like "5.0i", it is formatted to "5i"
        :param:
            num: Integer or float number
        :return:
            num: Integer or float number depending on whether the condition is met or not
    '''
    if num - int(num) == 0:
        return int(num)

    return num

def format_complx_ouput(num):

    real_prt, complx_prt = real_complx_sepration(num)
    real_is_zero = any([real_prt == '0', real_prt == '-0', real_prt == '+0'])
    cmplx_is_zero = any([complx_prt == '0', complx_prt == '-0', complx_prt == '+0'])
    if real_is_zero:
        return complx_prt + 'i'
    elif cmplx_is_zero:
        return real_prt
    elif real_is_zero and cmplx_is_zero:
        return '0'
    else:
        return num

def join_real_complx_prts(real_prt, complx_prt):

    if str(complx_prt)[0] != '-':
        complx_num = str(real_prt) + '+' + str(complx_prt) + 'i'
        return format_complx_ouput(complx_num)

    complx_num = str(real_prt) + str(complx_prt) + 'i'
    return format_complx_ouput(complx_num)

def trim_sign(num):

    num = re.sub(r'\+|-', '', num)
    return num

def join_uppr_lwr_terms(uppr_prt, lwr_prt):

    sign = str(float(uppr_prt)*float(lwr_prt))[0]
    if sign != '-':
        sign = ''

    if uppr_prt != lwr_prt:
        frction = sign + '('+ trim_sign(uppr_prt) + '/' + trim_sign(lwr_prt) + ')'
    else:
        # (n/n) = n
        frction = sign + trim_sign(uppr_prt)

    return frction

def calc_primes(lim_num):
    for prime in range(2, lim_num):
        for div in range(2, prime):
            if prime % div == 0:
                prime += 1
                break
        else:
            yield prime

def smplfy_frctions(uppr_part, lwr_part):
    sign_uppr_part = ''
    sign_lwr_part = ''

    if uppr_part.startswith('-'):
        sign_uppr_part = '-'
        uppr_part = uppr_part[1:] # The simplifying process does not work with negative numbers

    if lwr_part.startswith('-'):
        sign_lwr_part = '-'
        lwr_part = lwr_part[1:] # The simplifying process does not work with negative numbers

    uppr_part = int(uppr_part)
    lwr_part = int(lwr_part)
    smallr_num = 3
    while smallr_num > 2:
        if uppr_part > lwr_part:
            smallr_num = lwr_part
        else:
            smallr_num = uppr_part

        for prime_num in calc_primes(smallr_num):
            while uppr_part%prime_num == 0 and lwr_part%prime_num == 0:
                uppr_part /= prime_num
                lwr_part /= prime_num
        else:
            # If the prime number grows up to any smallr_num, then the fraction is not simplifiable
            # Appending the signs back
            uppr_part = sign_uppr_part + str(int(uppr_part))
            lwr_part = sign_lwr_part + str(int(lwr_part))
            return uppr_part, lwr_part

    # Appending the signs back
    uppr_part = sign_uppr_part + str(int(uppr_part))
    lwr_part = sign_lwr_part + str(int(lwr_part))
    return uppr_part, lwr_part

def LCM(num1, num2):
    '''
        Function to find the lowest common multiple (LCM) of two numbers
        :param:
            num1, num2: Integer numbers
        :return:
            num: Integer representing the LCM of num1 and num2. Returns None if one of the numbers is zero
    '''
    if num1 == 0 or num2 == 0:
        return None

    if num1 < 0:
        num1 = num1 * -1
    elif num2 < 0:
        num2 = num2 * -1
    elif num1 < 0 and num2 < 0:
        num1 = num1 * -1
        num2 = num2 * -1

    if num1 < num2:
        lower = num1
        upper = num2
    else:
        lower = num2
        upper = num1

    mult_low = lower
    mult_upp = upper
    count_low = 1
    count_upp = 1
    while mult_low < mult_upp:
        if mult_low == mult_upp:
            break
        mult_low = lower*count_low
        count_low += 1
        if mult_low > mult_upp:
            count_upp += 1
            mult_upp = upper*count_upp

    return mult_low

def sum_frac(num1, num2):
    '''
        Function to add two fractions
        :param:
            num1, num2: Strings with the fractions
        :return:
            frac: Result in simplified fraction
    '''
    pass

def real_complx_sum(real_prt1, complx_prt1, real_prt2, complx_prt2):
    # NOTE TO MYSELF: What if there are decimals?
    real_prt = format_floatnum(float(real_prt1) + float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) + float(complx_prt2))

    return join_real_complx_prts(real_prt, complx_prt)

def real_complx_subs(real_prt1, complx_prt1, real_prt2, complx_prt2):
    # NOTE TO MYSELF: What if there are decimals?

    real_prt = format_floatnum(float(real_prt1) - float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) - float(complx_prt2))

    return join_real_complx_prts(real_prt, complx_prt)

def real_complx_mult(real_prt1, complx_prt1, real_prt2, complx_prt2):
    term1 = format_floatnum(float(real_prt1) * float(real_prt2))
    term2 = format_floatnum(float(real_prt1) * float(complx_prt2))
    term3 = format_floatnum(float(complx_prt1) * float(real_prt2))
    term4 = -1 * format_floatnum(float(complx_prt1) * float(complx_prt2)) # Ends up being n*i^2 = -1*n = -n
    real_prt = term1 + term4
    complx_prt = term2 + term3

    return join_real_complx_prts(real_prt, complx_prt)

def real_complx_div(num_1, num_2, real_prt1, complx_prt1, real_prt2, complx_prt2):

    if real_prt1 == '0' and complx_prt1 == '0':
        return '0'
    if real_prt2 == '0' and complx_prt2 == '0':
        raise Exception('No number is divisible by zero')

    complx_prt_conjug = str(format_floatnum(float(complx_prt2) * -1)) # For the complex conjugate of num_2 (complx_conj_2)
    complx_conj_2 = join_real_complx_prts(real_prt2, complx_prt_conjug)
    # The formula of the complex division is (num1/num2) * (complx_conj_2/complx_conj_2)
    uppr_term = real_complx_mult(num_1, complx_conj_2)
    lowr_term = real_complx_mult(num_2, complx_conj_2) # This result is always a non-complex number

    uppr_term_real_prt,  uppr_term_cmplx_prt = real_complx_sepration(uppr_term)

    if lowr_term == '0':
        return '0'
    elif uppr_term_real_prt == '0':
        real_prt = '0'
        uppr_term_cmplx_prt, lowr_term = smplfy_frctions(uppr_term_cmplx_prt, lowr_term)
        complx_prt = join_uppr_lwr_terms(uppr_term_cmplx_prt, lowr_term)
    elif uppr_term_cmplx_prt == '0':
        uppr_term_real_prt, lowr_term = smplfy_frctions(uppr_term_real_prt, lowr_term)
        real_prt = join_uppr_lwr_terms(uppr_term_real_prt, lowr_term)
        complx_prt = '0'
    else:
        # No zeroes anywhere
        uppr_term_real_prt, lowr_term_symplfied = smplfy_frctions(uppr_term_real_prt, lowr_term)
        uppr_term_cmplx_prt, _ = smplfy_frctions(uppr_term_cmplx_prt, lowr_term)
        real_prt = join_uppr_lwr_terms(uppr_term_real_prt, lowr_term_symplfied)
        complx_prt = join_uppr_lwr_terms(uppr_term_cmplx_prt, lowr_term_symplfied)

    return join_real_complx_prts(real_prt, complx_prt)

if __name__ == '__main__':
    # Just for testing
    num1 = 1; num2 = 1
    lcm = LCM(num1, num2)
    print(f'The LCM between {num1} and {num2} is {lcm}')
    # num_2 = '(5/1)'
    # num_1 = '4+8i'
    # real_prt1, complx_prt1 = real_complx_sepration(num_1)
    # print('The real part is: ', real_prt1)
    # print('The complex part is: ', complx_prt1)
    # print('The middle sign is: ', search_middle_sign(num_1))
    # result = real_complx_sum(num_1, num_2)
    # print('The result of the sum is: ', result)
    # result = real_complx_subs(num_1, num_2)
    # print('The result of the subtraction is: ', result)
    # result = real_complx_mult(num_1, num_2)
    # print('The result of the multiplication is: ', result)
    # result = real_complx_div(num_1, num_2)
    # print('The result of the division is: ', result)