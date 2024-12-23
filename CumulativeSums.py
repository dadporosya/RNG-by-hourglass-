# TESTED
from numpy import zeros as zeros
from numpy import abs as abs
from numpy import max as max
from math import sqrt
from methods import *
from scipy.stats import norm #norm.cdf
from numpy import floor as floor

def CumulativeSums(sequence, mode=0, debug=False):
    """mode = 0 - forward
    mode = 1 - reverse"""
    n = len(sequence)
    if n < 10**6:
        return -1

    # First solution (problem: very slow):

    # 1 = +1; 0 = -1
    # sequence = plus_minus(sequence)
    # # print(sequence)
    # S_values = []
    # # print(Sn)
    # if mode == 1:
    #     sequence = sequence[::-1]
    #
    # print(sum(sequence))
    # for i in range(n):
    #     # print(i)
    #     S_values.append(abs(sum(sequence[0:i+1])))
    #

    # Second solution (problem: doesn't work, I don't know why):

    # S_max = 0
    # S_sum_now = 0
    # if sequence == "0":
    #     S_max = -1
    #
    # for i in sequence:
    #     i = int(i)
    #     if i == 0:
    #         i = -1
    #     S_sum_now += i
    #     S_max = max([S_max, S_sum_now])

    # print(S_values)
    # z = max(S_values)

    # Third solution (from the GitHub):

    counts = zeros(n)

    # Determine whether forward or backward data
    if mode == 1:
        sequence = sequence[::-1]

    counter = 0
    for char in sequence:
        sub = 1
        if char == '0':
            sub = -1
        if counter > 0:
            counts[counter] = counts[counter - 1] + sub
        else:
            counts[counter] = sub

        counter += 1


    z = max(abs(counts))


    k1 = int(((-1*n/z)+1)/4)
    k2 = int(((-1 * n / z) - 3) / 4)
    k_max = int(((n/z)-1) / 4)

    Pvalue = 1
    sum_k1 = 0
    sum_k2 = 0

    k = k1
    while k <= k_max:
        sum_k1 += abs(norm.cdf(((4 * k + 1) * z)/sqrt(n)) - norm.cdf(((4 * k - 1) * z)/sqrt(n)))
        k += 1

    k = k2
    while k <= k_max:
        sum_k2 += abs(norm.cdf(((4 * k + 3) * z) / sqrt(n)) - norm.cdf(((4 * k + 1) * z) / sqrt(n)))
        k += 1


    if debug:
        print(f'S max = {z}')
        print(f'Sum 1 = {sum_k1}')
        print(f'Sum 2 = {sum_k2}')
        print()


    Pvalue -= sum_k1
    Pvalue += sum_k2
    return Pvalue


# sequence = generate_pseudo_random(10**3)
# sequence = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
# # sequence = "1101100110110000011010001100011111000111101000110001000000000010101011111101101110110001000111110001100011001100110000000000100001101001011110111111101010110011111100011011010010000000000110000011000001101001100111111110000110010100101011100000000001101110101100001110000010100110011011001000001101000100000000011010101101110110000011100010100101000101011101011001000001000010000001110001100100010111101110010010111110110000000000001110000001010001111011010010110001100110001011001100000000000010001010010111101001011001100011000101001000111010010000000000111111101000000010110101001011001000011111110000111010000000001100110100101110100100011100000011000010100101100010000000000110100100100011001011010001100100000101000111001001000000000000010101101000001111111010101000111100000100111010010000000000010111110101000010000001010111110011011001011111010000000000000001000001100100111100000110001011011110100111011000111100000000001111111010100001010100101000111111100100011111110001100000000010100100"
# print(sequence)

# with open("../sequence.txt", "r") as file:
#     sequence = file.readline()
# print(CumulativeSums(sequence, 0))
# print(CumulativeSums(sequence, 1))
