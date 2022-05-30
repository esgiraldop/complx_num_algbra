def real_complx_sepration(num):
    real_prt = num_1.split('+')[0]
    complx_part = num_1.split('+')[1].split('i')[0]
    return real_prt, complx_part

def real_sum(num_1, num_2):
    pass
    return result

def complx_sum(num_1, num_2):
    pass
    return result

def real_subs(num_1, num_2):
    pass
    return result

def complx_subs(num_1, num_2):
    pass
    return result

def real_complx_mult(num_1, num_2):
    pass
    return result

def real_complx_div(num_1, num_2):
    pass
    return result

if __name__ == '__main__':
    num_1 = '4+3i'
    num_2 = '5+3i'
    real_prt, complx_part = real_complx_sepration(num_1)
    print('The real part is: ', real_prt)
    print('The complex part is: ', complx_part)