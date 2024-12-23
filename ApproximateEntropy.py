from scipy.special import gammaincc
# from mpmath import gammaincc
from math import log
from methods import *
def ApproximateEntropy(sequence, m=10, debug=False):
    """
    ApproximateEntropy test
    m - length of each block
    """
    _ = log(3000, 2) - 5
    if _ < m:
        m = int(_) - 1
        print(f"m = {m}; _ = {_}")

    n = len(sequence)
    extended_sequence = sequence + sequence[0:m-1]
    # print(extended_sequence)
    ext_n = len(extended_sequence)


    i_values = {}
    i_plus_1_values = {}

    v_m = m
    v_m1 = m + 1

    for i in range(ext_n):
        try:
            if not i + v_m >= ext_n:
                i_values[extended_sequence[i:i + v_m]] += 1
        except:
            i_values[extended_sequence[i:i + v_m]] = 1

        try:
            if not i + v_m1 >= ext_n:
                i_plus_1_values[extended_sequence[i:i + v_m1]] += 1
        except:
            i_plus_1_values[extended_sequence[i:i + v_m1]] = 1

    C_values = [i/n for i in list(i_values.values())]
    C_plus_1_values = [i / n for i in list(i_plus_1_values.values())]

    phi_m = 0
    phi_m_plus_1 = 0

    for pi_j in C_values:
        if pi_j > 0:
            phi_m += pi_j * log(pi_j)

    for pi_j in C_plus_1_values:
        if pi_j > 0:
            phi_m_plus_1 += pi_j * log(pi_j)

    ApEn_m = phi_m - phi_m_plus_1

    X2 = 2 * n * (log(2) - ApEn_m)

    if debug:
        print(f'phi_m = {phi_m}; phi_m+1 = {phi_m_plus_1}')
        print(f'ApEn_m = {ApEn_m}')
        print(f'X2 = {X2}')
        print()

    Pvalue = float(gammaincc(2 ** (m-1), X2 / 2))

    return Pvalue