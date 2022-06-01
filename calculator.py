import re

def search_middle_sign(num):
    sign = re.search(r'\d*\.?\d*(\+|-)\d*\.?\d*i', num).groups()[0]
    return sign

def real_complx_sepration(num):
    pattern = r'((?:\+|-)?\d*\.?\d*)((?:\+|-)?\d*\.?\d*)i'
    real_prt = re.search(pattern, num).groups()[0]
    complx_part = re.search(pattern, num).groups()[1]
    return real_prt, complx_part

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

def multply_signs(num, sign):

    return num

def real_complx_sum(num_1, num_2):
    # NOTE TO MYSELF: What if there are decimals?
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    real_prt = format_floatnum(float(real_prt1) + float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) + float(complx_prt2))

    if str(complx_prt)[0] != '-':
        return str(real_prt) + '+' + str(complx_prt) + 'i'

    return str(real_prt) + str(complx_prt) + 'i'

def real_complx_subs(num_1, num_2):
    # NOTE TO MYSELF: What if there are decimals?
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    real_prt = format_floatnum(float(real_prt1) - float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) - float(complx_prt2))

    if str(complx_prt)[0] != '-':
        return str(real_prt) + '+' + str(complx_prt) + 'i'

    return str(real_prt) + str(complx_prt) + 'i'

def real_complx_mult(num_1, num_2):
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    term1 = format_floatnum(float(real_prt1) * float(real_prt2))
    term2 = format_floatnum(float(real_prt1) * float(complx_prt2))
    term3 = format_floatnum(float(complx_prt1) * float(real_prt2))
    term4 = -1 * format_floatnum(float(complx_prt1) * float(complx_prt2)) # Ends up being n*i^2 = -1*n = -n
    real_prt = term1 + term4
    complx_prt = term2 + term3

    if str(complx_prt)[0] != '-':
        return str(real_prt) + '+' + str(complx_prt) + 'i'

    return str(real_prt) + str(complx_prt) + 'i'

def real_complx_div(num_1, num_2):
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    complx_conjugate = str(real_prt) + ' + ' + str(complx_prt) + 'i'

    return result

if __name__ == '__main__':
    num_1 = '4+8i'
    num_2 = '5+10i'
    # num_1 = '-4-8i'
    # real_prt1, complx_part1 = real_complx_sepration(num_1)
    # print('The real part is: ', real_prt1)
    # print('The complex part is: ', complx_part1)
    # print('The middle sign is: ', search_middle_sign(num_1))
    result = real_complx_sum(num_1, num_2)
    print('The result of the sum is: ', result)
    result = real_complx_subs(num_1, num_2)
    print('The result of the subtraction is: ', result)
    result = real_complx_mult(num_1, num_2)
    print('The result of the multiplication is: ', result)