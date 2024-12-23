from scipy.special import gammaincc
from methods import *

def BlockFrequency(sequence, M=128, debug=False):
    n = len(sequence)
    # choose M (len of each block), if it's undefined
    if not M:
        if 20 < 0.01 * n:
            M = 0.01 * n
        else:
            M = 20

    # divide sequence into M blocks
    blocks = divide_str_to_list(sequence, M)
    N = len(blocks)
    pi_values = []
    for block in blocks:
        pi_values.append(sum(block) / M)

    pi_sum = 0
    for pi in pi_values:
        pi_sum += (pi - 0.5) ** 2

    X2obs = 4 * M * pi_sum


    if debug:
        print(f'pi_sum = {pi_sum}')
        print(f'X2obs = {X2obs}')
        print()

    Pvalue = gammaincc(N/2, X2obs/2)
    return Pvalue
