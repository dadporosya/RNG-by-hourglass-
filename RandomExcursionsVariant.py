# TESTED

from methods import *
from scipy.special import erfc
# from scipy.special import gammaincc
from numpy import sqrt
# from numpy import append as append
from numpy import cumsum as cumsum



def RandomExcursionsVariant(sequence, debug=False):
    """mode = 0 - forward
    mode = 1 - reverse"""
    n = len(sequence)
    if n < 10*6:
        return -1

    # 1 = +1; 0 = -1
    sequence = plus_minus(sequence)
    # print(sequence)
    # Compute partial sums Si of successively larger subsequences, each starting with x1. Form the set S
    S = cumsum(sequence)

    J = list(S).count(0)+1

    S_set = sorted(set(S))

    S = list(S)

    Pvalues = []
    for x in S_set:
        # if debug:
        #     print(f"x = {x}")
        if x == 0:
            continue
        elif abs(x) <= 9:
            # print(x, S.count(x))
            dividend = abs(S.count(x) - J)
            divider = sqrt(2 * J * (4 * abs(x) - 2))
            # print(x, S.count(x), dividend, divider)
            print(dividend / divider)
            Pvalues.append(float(erfc(dividend / divider)))


    return Pvalues





# # sequence = generate_pseudo_random(10**3)
# # sequence = "0110110101"
# sequence = '11011001101100000110100011000111110001111010001100010000000000101010111'
# # sequence = "1101100110110000011010001100011111000111101000110001000000000010101011111101101110110001000111110001100011001100110000000000100001101001011110111111101010110011111100011011010010000000000110000011000001101001100111111110000110010100101011100000000001101110101100001110000010100110011011001000001101000100000000011010101101110110000011100010100101000101011101011001000001000010000001110001100100010111101110010010111110110000000000001110000001010001111011010010110001100110001011001100000000000010001010010111101001011001100011000101001000111010010000000000111111101000000010110101001011001000011111110000111010000000001100110100101110100100011100000011000010100101100010000000000110100100100011001011010001100100000101000111001001000000000000010101101000001111111010101000111100000100111010010000000000010111110101000010000001010111110011011001011111010000000000000001000001100100111100000110001011011110100111011000111100000000001111111010100001010100101000111111100100011111110001100000000010100100"
# print(sequence)
# with open("../sequence.txt", "r") as file:
#     sequence = file.readline()
#
# Pvalues = RandomExcursionsVariant(sequence, debug=True)
# for P in Pvalues:
#     print(f"{P[0]}: Pvalue:{P[1]}")
#     # print(f"Pvalue:{Pvalues[1]}")

# 0.18190171877724973
# 0.06454972243679027
# 0.06933752452815364
# 0.07537783614444091
# 0.25
# 0.472455591261534
# 0.8944271909999159
# 1.0103629710818451
# 0.25
# 0.5

# 0.18190171877724973
# 0.06454972243679027
# 0.06933752452815364
# 0.07537783614444091
# 0.25
# 0.472455591261534
# 0.8944271909999159
# 1.0103629710818451
# 0.25
# 0.5

# ('-9.0', np.float64(-9.0), 18, np.float64(0.05234506327316326), np.True_)
# ('-8.0', np.float64(-8.0), 16, np.float64(0.07070114486598304), np.True_)
# ('-7.0', np.float64(-7.0), 16, np.float64(0.05220363534131463), np.True_)
# ('-6.0', np.float64(-6.0), 21, np.float64(0.004178557568166483), np.False_)
# ('-5.0', np.float64(-5.0), 24, np.float64(0.00024573277993030363), np.False_)
# ('-4.0', np.float64(-4.0), 14, np.float64(0.023342202012890823), np.True_)
# ('-3.0', np.float64(-3.0), 6, np.float64(0.37109336952269756), np.True_)
# ('-2.0', np.float64(-2.0), 5, np.float64(0.3864762307712327), np.True_)
# ('-1.0', np.float64(-1.0), 3, np.float64(0.6170750774519739), np.True_)
# ('+1.0', np.float64(1.0), 1, np.float64(0.6170750774519739), np.True_)