#TESTED

from scipy.special import gammaincc

from methods import *
def NonOverlappingTemplateMatching(sequence, B="000000001", M = 8, debug = False):
    """B - шаблон
    M - length of each block"""
    n = len(sequence)

    m = len(B)
    N = int(n / M)
    # while True:
    #      #len of each block
    #     if M < n * 0.01:
    #         N /= 2
    #         M = int(n / N)
    #     else:
    #         break

    sequence = divide_str_to_str(sequence, N)

    matches = [] # W values
    for block in sequence:
        j = 0
        Wj = 0
        while j + m - 1 < N:
            if block[j:j+m] == B:
                Wj += 1
                j += m
            else:
                j += 1
        matches.append(Wj)

    mu = (N - m + 1) / (2**m)

    sigma_sq = N * ((1 / (2**m)) - ((2*m - 1)/(2 ** (2 * m))))


    X2obs = 0
    for Wj in matches:
        X2obs += ((Wj - mu)**2) / sigma_sq

    if debug:
        print(f"mu = {mu}")
        print(f"sigma_sq = {sigma_sq}")
        print(f"X2obs = {X2obs}")
        print()

    Pvalue = gammaincc(M/2, X2obs/2)
    return Pvalue

# with open("../sequence.txt", "r") as file:
#     sequence = file.readline()
# #
# print(NonOverlappingTemplateMatching(sequence))

# # sequence = "1110001011001101110110011111111101000101100101111100000000000010110000101000001010100011000111110011110110010000110000000000000101010001010011011011000010101110110011101110100001000000001001010000111100101001100011111110011011010010100101100001001001101000001101001101000011101110110110011000011100000000000011110010111001111100000010100110100011011110101100100000000000101000001110101001100110000000010110001110011111110000000000000011111100110001110101101001001000100000100100111011101000000000100001100111100000100100110110001000000111100010100110000000000010001101111011110100000001100100101100010111111011000000000001011101011001111110111010011010001101111111110111101000000000010101111001111001001110101000010011110110001001001000000000000110000001010011000101001100001100100011110011110010110000000110100111110001001000110010010110110011000011000011100000000010010110010110001101010111110100011110001000000110000000000000110100011010111011010000000100101101000111011101001000000000001001010111"
# sequence = generate_pseudo_random(10**3)
# print(sequence)
# print(NonOverlappingTemplateMatching(sequence))