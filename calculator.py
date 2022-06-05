import re

def search_middle_sign(num):
    sign = re.search(r'\d*\.?\d*(\+|-)\d*\.?\d*i', num).groups()[0]
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
    pattern1 = r'^(?:\+|-)?\d*\.?\d*i'

    # pattern2 = r'(?:(?:\+|-)?\d*\.?\d*)$' # Old pattern
    pattern2 = r'(?:\+|-)?\d*\.?\d*[^i]$' # Best pattern so far
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
        # pattern3 = r'((?:\+|-)?\d*\.?\d*)((?:\+|-)?\d*\.?\d*)i' # Previous pattern3. Do not work for only real numbers
        pattern3 = r'((?:\+|-)?\d*\.?\d*)((?:\+|-)?\d*\.?\d*)i?' # Current best pattern
        real_prt = re.search(pattern3, num).groups()[0]
        complx_prt = re.search(pattern3, num).groups()[1]
    if complx_prt == '-' or complx_prt == '+': # In case the user enters for example 1+i or 1-i or 34.56+i
        complx_prt = complx_prt + '1'

    real_prt, complx_prt = str(format_floatnum(float(real_prt))), str(format_floatnum(float(complx_prt)))

    # The next pattern could be use for matching input numbers like "-0", "+0", "-000.0000", and then add more lines of
        # code to formatting every similar input to a simple "0", but as the output numbers here are intended to be
        # entered in float() function within other functions that call the present one, this is simply not necessary
    # pattern4 = r'^(?:(?:\+|-)?0*\.?0*)'
    return real_prt, complx_prt

def decimal_2_frac(num):
    ''' Function to transform from decimal to fraction'''
    pass
    return frac

def format_floatnum(num):
    '''
        Function for formatting numbers. If there is a number like "5.0i", it is formatted to "5i"
        :param num:
        :return:
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

def multply_signs(real_prt, complx_prt):

    if str(complx_prt)[0] != '-':
        complx_num = str(real_prt) + '+' + str(complx_prt) + 'i'
        return format_complx_ouput(complx_num)

    complx_num = str(real_prt) + str(complx_prt) + 'i'
    return format_complx_ouput(complx_num)

def real_complx_sum(num_1, num_2):
    # NOTE TO MYSELF: What if there are decimals?
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    real_prt = format_floatnum(float(real_prt1) + float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) + float(complx_prt2))

    return multply_signs(real_prt, complx_prt)

def real_complx_subs(num_1, num_2):
    # NOTE TO MYSELF: What if there are decimals?
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    real_prt = format_floatnum(float(real_prt1) - float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) - float(complx_prt2))

    return multply_signs(real_prt, complx_prt)

def real_complx_mult(num_1, num_2):
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    term1 = format_floatnum(float(real_prt1) * float(real_prt2))
    term2 = format_floatnum(float(real_prt1) * float(complx_prt2))
    term3 = format_floatnum(float(complx_prt1) * float(real_prt2))
    term4 = -1 * format_floatnum(float(complx_prt1) * float(complx_prt2)) # Ends up being n*i^2 = -1*n = -n
    real_prt = term1 + term4
    complx_prt = term2 + term3

    return multply_signs(real_prt, complx_prt)

def real_complx_div(num_1, num_2):
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)

    if real_prt1 == '0' and complx_prt1 == '0':
        return '0'
    if real_prt2 == '0' and complx_prt2 == '0':
        raise Exception('No number can be divided by zero')

    complx_prt_conjug = str(format_floatnum(float(complx_prt2) * -1)) # For the complex conjugate of num_2 (complx_conj_2)
    complx_conj_2 = multply_signs(real_prt2, complx_prt_conjug)
    # The formula of the complex division is (num1/num2) * (complx_conj_2/complx_conj_2)
    uppr_term = real_complx_mult(num_1, complx_conj_2)
    lowr_term = real_complx_mult(num_2, complx_conj_2) # This result is always a non-complex number

    uppr_term_real_prt,  uppr_term_cmplx_prt = real_complx_sepration(uppr_term)

    if lowr_term == '0':
        return '0'
    elif uppr_term_real_prt == '0':
        real_prt = '0'
        complx_prt = '(' + uppr_term_cmplx_prt + '/' + lowr_term + ')'
    elif uppr_term_cmplx_prt == '0':
        real_prt = uppr_term_real_prt + '/' + lowr_term
        complx_prt = '0'
    else:
        # No zeroes anywhere
        real_prt = uppr_term_real_prt + '/' + lowr_term
        complx_prt = '(' + uppr_term_cmplx_prt + '/' + lowr_term + ')i'

    return multply_signs(real_prt, complx_prt)

if __name__ == '__main__':
    num_2 = '4-8i'
    num_1 = '4+8i'
    # num_1 = '-0-0i'
    # real_prt1, complx_prt1 = real_complx_sepration(num_1)
    # print('The real part is: ', real_prt1)
    # print('The complex part is: ', complx_prt1)
    # print('The middle sign is: ', search_middle_sign(num_1))
    # result = real_complx_sum(num_1, num_2)
    # print('The result of the sum is: ', result)
    result = real_complx_subs(num_1, num_2)
    print('The result of the subtraction is: ', result)
    # result = real_complx_mult(num_1, num_2)
    # print('The result of the multiplication is: ', result)
    # result = real_complx_div(num_1, num_2)
    # print('The result of the division is: ', result)