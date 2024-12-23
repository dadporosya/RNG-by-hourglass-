#TESTED
from math import log, sqrt
from scipy.special import erfc
from methods import *
def Universal(sequence, debug=False):
    """L - lenth of each block
    Q - the number of blocks in initialization segment
    K - the number of blocks in test segment"""
    if debug:
        print("Universal")

    # L values depending on n
    # n: L,
    L_VALUES = {
        387840: 6,
        904960: 7,
        2068480: 8,
    }

    # expected values depending on L
    # L: [expectedValues, variance]
    EXPECTED_VALUES = {
        6: [5.2177052, 2.954],
        7: [6.1962507, 3.125],
        8: [7.1836656, 3.238]
    }



    n = len(sequence)
    if n < min(list(L_VALUES.keys())):
        print('Too low sequence size')
        return -1
    for key in list(L_VALUES.keys()):
        if n >= key:
            L = L_VALUES[key]
        else:
            break

    expectedValue = EXPECTED_VALUES[L][0]
    variance = EXPECTED_VALUES[L][1]

    Q = 10 * 2 ** L
    K = int((n / L) - Q)

    Q_segment, K_segment = divide_in_2_segments(sequence, L, Q)
    # print(Q_segment, K_segment)
    # print(len(Q_segment), len(K_segment))

    L_variants = all_possible_variants(L)
    zero_list = [0] * len(L_variants)

    L_variants = dict(zip(L_variants, zero_list))
    # print(L_variants)

    for i in range(Q):
        block = Q_segment[i]
        L_variants[block] = i+1

    # print(Q_segment)
    # print(L_variants)

    fn = 0
    for i in range(len(K_segment)):
        block = K_segment[i]
        i += 1 + Q

        # print(i, L_variants[block])
        difference = i - L_variants[block]
        if difference != 1:
            fn += log(i - L_variants[block], 2)
        L_variants[block] = i

    fn /= K

    # print(fn)
    c = 0.7
    c -= 0.8/L
    c += (4 + 32 / L) * (K ** (-3/L) / 15)

    sigma = c * sqrt(variance/K)

    if debug:
        print(f"c = {c}")
        print(f"sigma = {sigma}")
        print(f"K = {K}")
        print(f"fn = {fn}")
        print(f"fn * K = {fn * K}")

    Pvalue = erfc(abs((fn - expectedValue)/(sqrt(2) * sigma)))
    return Pvalue


#

# sequence = generate_pseudo_random(600000) # min length: 387840
# print(sequence)
# print(Universal(sequence))
# print(OverlappingTemplateMatching(input(), input(), int(input())))