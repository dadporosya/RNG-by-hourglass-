#TESTED
from scipy.special import gammaincc
# from mpmath import gammaincc
from methods import *
def OverlappingTemplateMatching(sequence, B="111111111", N = 1032, debug=False):
    """B - template (шаблон) (recommended: 9 or 10)
    N - length of each block (> 50)"""

    # pi values, if n >= 10**6
    PI_VALUES = {
        0: 0.364091,
        1: 0.185659,
        2: 0.139381,
        3: 0.100571,
        4: 0.0704323,
        5: 0.139865
    }


    n = len(sequence)
    m = len(B)
    M = int(n / N)

    sequence = divide_str_to_str(sequence, N)

    matches = [] # W values
    for block in sequence:
        i = 0
        vi = 0
        while i + m - 1 < M:
            if block[i:i+m] == B:
                vi += 1
            i += 1
        if vi > 5:
            vi = 5
        matches.append(vi)


    vi_values = []
    for i in range(6): # 0 1 2 3 4 5
        vi_values.append(matches.count(i))
    # vi_values = [matches.count(0), matches.count(1), matches.count(2), matches.count(3), matches.count(4), matches.count(5)]

    # lambda_ = (M - m + 1) / (2**m)
    # eta = lambda_ / 2

    X2obs = 0
    for i in range(len(vi_values)):
        vi = vi_values[i]
        pi = PI_VALUES[i]
        X2obs += ((vi - (N * pi)) ** 2) / (N * pi)

    if debug:
        print(f"vi values = {vi_values}")
        print(f"X2obs = {X2obs}")
        print()

    Pvalue = gammaincc(5/2, X2obs/2)


    return Pvalue






# # sequence = "1110001011001101110110011111111101000101100101111100000000000010110000101000001010100011000111110011110110010000110000000000000101010001010011011011000010101110110011101110100001000000001001010000111100101001100011111110011011010010100101100001001001101000001101001101000011101110110110011000011100000000000011110010111001111100000010100110100011011110101100100000000000101000001110101001100110000000010110001110011111110000000000000011111100110001110101101001001000100000100100111011101000000000100001100111100000100100110110001000000111100010100110000000000010001101111011110100000001100100101100010111111011000000000001011101011001111110111010011010001101111111110111101000000000010101111001111001001110101000010011110110001001001000000000000110000001010011000101001100001100100011110011110010110000000110100111110001001000110010010110110011000011000011100000000010010110010110001101010111110100011110001000000110000000000000110100011010111011010000000100101101000111011101001000000000001001010111"
# sequence = generate_pseudo_random(10**6)
# print(sequence)
# print(OverlappingTemplateMatching(sequence))