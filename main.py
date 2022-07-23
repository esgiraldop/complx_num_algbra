'''Complex Number Algebra - Program that carries out addition, subtraction, multiplication and division of complex
    numbers.'''
import ask_usr
import calculator as calc

# Asking for the two complex numbers
num_1 = ask_usr.ask_num()
num_2 = ask_usr.ask_num()

# Separating real and complex parts
real_prt1, complx_prt1 = real_complx_sepration(num_1)
real_prt2, complx_prt2 = real_complx_sepration(num_2)
# Transforming into fractions.


# Carrying out the four operations between the complex numbers entered by the user
sum_ans = calc.real_complx_sum(real_prt1, complx_prt1, real_prt2, complx_prt2)
subs_ans = calc.real_complx_subs(real_prt1, complx_prt1, real_prt2, complx_prt2)
mult_ans = calc.real_complx_mult(real_prt1, complx_prt1, real_prt2, complx_prt2
div_ans = calc.real_complx_div(frac_1, frac_2, real_prt1, complx_prt1, real_prt2, complx_prt2)

print(f'The result for the addition between {num_1} and {num_2} is {sum_ans}')
print(f'The result for the subtraction between {num_1} and {num_2} is {subs_ans}')
print(f'The result for the multiplication between {num_1} and {num_2} is {mult_ans}')
print(f'The result for the division between {num_1} and {num_2} is {div_ans}')