#TESTED
from scipy.special import gammaincc
# from mpmath import gammaincc
from methods import *
def Serial(sequence, m=16, debug=False):
    """m - length of each block"""
    if debug:
        print("Serial")

    n = len(sequence)
    extended_sequence = sequence + sequence[0:m-1]
    # print(extended_sequence)
    ext_n = len(extended_sequence)


    v_values = {}
    v_minus_1_values = {}
    v_minus_2_values = {}

    v_m = m
    v_m1 = m - 1
    v_m2 = m - 2


    for i in range(ext_n):
        try:
            if not i + v_m >= ext_n:
                v_values[extended_sequence[i:i+v_m]] += 1
        except:
            v_values[extended_sequence[i:i+v_m]] = 1

        try:
            if not i + v_m1 >= ext_n:
                v_minus_1_values[extended_sequence[i:i+v_m1]] += 1
        except:
            v_minus_1_values[extended_sequence[i:i+v_m1]] = 1

        try:
            if not i + v_m2 >= ext_n:
                v_minus_2_values[extended_sequence[i:i+v_m2]] += 1
        except:
            v_minus_2_values[extended_sequence[i:i+v_m2]] = 1
    #
    # print(v_values)
    # print(v_minus_1_values)
    # print(v_minus_2_values)

    psi2m = 0
    for vi in list(v_values.values()):
        psi2m += vi**2
    psi2m *= 2**m / n
    psi2m -= n

    psi2m_minus_1 = 0
    for vi1 in list(v_minus_1_values.values()):
        psi2m_minus_1 += vi1 ** 2
    psi2m_minus_1 *= 2 ** (m-1) / n
    psi2m_minus_1 -= n

    psi2m_minus_2 = 0
    for vi2 in list(v_minus_2_values.values()):
        psi2m_minus_2 += vi2 ** 2
    psi2m_minus_2 *= 2 ** (m - 2) / n
    psi2m_minus_2 -= n

    delta_psi2_m = psi2m - psi2m_minus_1
    delta2_psi2_m = psi2m - 2*psi2m_minus_1 + psi2m_minus_2

    if debug:
        print("Psi values: ", psi2m, psi2m_minus_1, psi2m_minus_2)
        print("Sums: ", delta_psi2_m, delta2_psi2_m)
        print()

    Pvalue1 = float(gammaincc(2**(m-2), delta_psi2_m /2))
    Pvalue2 = float(gammaincc(2 ** (m - 3), delta2_psi2_m /2))


    return [Pvalue1, Pvalue2]


# sequence = generate_pseudo_random(10**6)
# print(sequence)
#
# with open("../sequence.txt", "r") as file:
#     sequence = file.readline()
# #
# print(Serial(sequence))
# print(Serial("0011011101", 3))
# 67091.904 34520.512 18021.824

# 67091.904 34520.512 18021.824
# 32571.391999999993 50593.21599999999
# (0.7784401931558558, 0.9579169429835735)

# Serial Test DEBUG BEGIN:
# 	Length of input:	 1000000
# 	Value of Sai:		 [2790220.296192 2516154.118144 2258447.888384]
# 	Value of Nabla:		 274066.1780480002 16359.948288000189
# 	P-Value 01:			 0.0
# 	P-Value 02:			 0.5514200656675974