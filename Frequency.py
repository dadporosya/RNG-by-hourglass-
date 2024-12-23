# TESTED

from math import sqrt
from scipy.special import erfc
from methods import *


def Frequency(sequence, debug = False):
    n = len(sequence)

    # 1 = +1; 0 = -1
    S = plus_minus(sequence)
    Sn = sum(S)
    # print(Sn)
    Sobs = abs(Sn)/sqrt(n)
    # print(Sobs)
    Pvalue = erfc(Sobs/sqrt(2))

    if debug:
        print('Frequency')
        print(f'Sn = {Sn}')
        print(f'Sobs = {Sobs}')
        print()

    return Pvalue

# # 1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000, P = 0.10959
# sequence = generate_pseudo_random(10**3)
# print(sequence)
# # sequence = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
# print(Frequency(sequence)) #0.00014780231033445455