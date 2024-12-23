# TESTED

from methods import *
from scipy.special import gammaincc
from numpy import append as append
from numpy import cumsum as cumsum

def get_pi_value(k, x):
    pi = None
    if k == 0:
        pi = 1 - 1/(2*abs(x))
    elif k in [1, 2, 3, 4]:
        pi = (1/(4*x**2)) * (1 - 1/(2*abs(x))) ** (k-1)
    elif k >= 5:
        pi = (1/(2*abs(x))) * (1 - 1/(2*abs(x))) ** 4
    return pi

def k_frequency(block, k):
    return block.count(k)

def RandomExcursions(sequence, debug=False):
    """mode = 0 - forward
    mode = 1 - reverse"""
    n = len(sequence)

    # 1 = +1; 0 = -1
    sequence = plus_minus(sequence)
    # print(sequence)
    # # print(sum(sequence))
    # for i in range(n):
    #     S.append(sum(sequence[0:i+1]))

    # Compute partial sums Si of successively larger subsequences, each starting with x1. Form the set S
    cumulative_sum = cumsum(sequence)

    # Form a new sequence S' by attaching zeros before and after the set S. That is, S' = 0, s1, s2, … , sn, 0.
    S = append(cumulative_sum, [0])
    S = append([0], S)
    # print(cumulative_sum)
    # print(cumulative_sum[4] + 1)

    J = list(S).count(0) - 1

    sub_lists = [[]]
    index = 0
    zero_counter = 0
    for i in S:
        if i == 0:
            zero_counter += 1
        elif zero_counter == 2:
            zero_counter = 1
            index += 1
            sub_lists.append([0])

        sub_lists[index].append(i)


    len_sub_lists = len(sub_lists)

    x_values = {
        -4: [0] * len_sub_lists,
        -3: [0] * len_sub_lists,
        -2: [0] * len_sub_lists,
        -1: [0] * len_sub_lists,
        1: [0] * len_sub_lists,
        2: [0] * len_sub_lists,
        3: [0] * len_sub_lists,
        4: [0] * len_sub_lists
    }

    keys = list(x_values.keys())

    i = 0
    for i in range(len_sub_lists):
        block = sub_lists[i]
        for x in block:
            if x in keys:
                x_values[x][i] = block.count(x)


    Pvalues = []
    X2_obses = []

    for list_ in x_values.items():
        X2_obs = 0
        x = list_[0]
        block = list_[1]
        for k in [0, 1, 2, 3, 4, 5]:
            Vk = k_frequency(block, k)
            pi = get_pi_value(k, x)
            _ = (Vk - J * pi)**2
            X2_obs += _ / (J * pi)
        X2_obses.append(X2_obs)
        Pvalues.append(float(gammaincc(2.5, X2_obs/2)))

    if debug:
        print(f"x values = {x_values}")


    return Pvalues




# # sequence = generate_pseudo_random(10**3)
# sequence = "0110110101"
# # sequence = "1101100110110000011010001100011111000111101000110001000000000010101011111101101110110001000111110001100011001100110000000000100001101001011110111111101010110011111100011011010010000000000110000011000001101001100111111110000110010100101011100000000001101110101100001110000010100110011011001000001101000100000000011010101101110110000011100010100101000101011101011001000001000010000001110001100100010111101110010010111110110000000000001110000001010001111011010010110001100110001011001100000000000010001010010111101001011001100011000101001000111010010000000000111111101000000010110101001011001000011111110000111010000000001100110100101110100100011100000011000010100101100010000000000110100100100011001011010001100100000101000111001001000000000000010101101000001111111010101000111100000100111010010000000000010111110101000010000001010111110011011001011111010000000000000001000001100100111100000110001011011110100111011000111100000000001111111010100001010100101000111111100100011111110001100000000010100100"
# print(sequence)
# with open("../sequence.txt", "r") as file:
#     sequence = file.readline()
# print(RandomExcursions(sequence))
# #
# # # print(Pvalues)
# l = [-4, -3, -2, -1, 1, 2, 3, 4]
# for i in range(len(Pvalues)):
#     print(f"{l[i]}:  Pvalue:{Pvalues[i]}")
