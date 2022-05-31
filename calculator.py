def real_complx_sepration(num):
    # NOTE TO MYSELF: what if there are decimals entered?
    real_prt = num.split('+')[0]
    complx_part = num.split('+')[1].split('i')[0]
    return real_prt, complx_part

def decimal_2_frac(num):
    ''' Function to transform from decimal to fraction'''
    pass
    return frac

def format_floatnum(num):
    if num - int(num) == 0:
        return int(num)

    return num

def real_complx_sum(num_1, num_2):
    # NOTE TO MYSELF: What if there are decimals?
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    real_prt = format_floatnum(float(real_prt1) + float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) + float(complx_prt2))
    # Formatting numbers. If there is a number like "5.0i", it is formatted to "5i"
    return str(real_prt) + ' + ' + str(complx_prt) + 'i'

def real_complx_subs(num_1, num_2):
    # NOTE TO MYSELF: What if there are decimals?
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    real_prt = format_floatnum(float(real_prt1) - float(real_prt2))
    complx_prt = format_floatnum(float(complx_prt1) - float(complx_prt2))
    # Formatting numbers. If there is a number like "5.0i", it is formatted to "5i"
    return str(real_prt) + ' + ' + str(complx_prt) + 'i'

def real_complx_mult(num_1, num_2):
    real_prt1, complx_prt1 = real_complx_sepration(num_1)
    real_prt2, complx_prt2 = real_complx_sepration(num_2)
    term1 = format_floatnum(float(real_prt1) * float(real_prt2))
    term2 = format_floatnum(float(real_prt1) * float(complx_prt2))
    term3 = format_floatnum(float(complx_prt1) * float(real_prt2))
    term4 = -1 * format_floatnum(float(complx_prt1) * float(complx_prt2)) # Ends up being n*i^2 = -1*n = -n
    real_prt = term1 + term4
    complx_prt = term2 + term3

    return str(real_prt) + ' + ' + str(complx_prt) + 'i'

def real_complx_div(num_1, num_2):
    pass
    return result

if __name__ == '__main__':
    num_1 = '4+8i'
    num_2 = '5+3i'
    # real_prt1, complx_part1 = real_complx_sepration(num_1)
    # print('The real part is: ', real_prt)
    # print('The complex part is: ', complx_part)
    result = real_complx_sum(num_1, num_2)
    print('The result of the sum is: ', result)
    result = real_complx_subs(num_1, num_2)
    print('The result the subtraction is: ', result)
    result = real_complx_mult(num_1, num_2)
    print('The result the multiplication is: ', result)