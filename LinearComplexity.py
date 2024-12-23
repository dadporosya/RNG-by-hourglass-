#TESTED

from scipy.special import gammaincc
# from mpmath import gammaincc
from methods import *
def LinearComplexity(sequence, M=1000, debug=False):
    """M - length of each block
    N - the number of blocks"""

    PI_VALUES = {
        0: 0.010417,
        1: 0.03125,
        2: 0.125,
        3: 0.5,
        4: 0.25,
        5: 0.0625,
        6: 0.020833
    }
# 0.010417, π1 = 0.03125, π2 = 0.125, π3 = 0.5, Nπ i=0 i π4 = 0.25,π5 = 0.0625, π6 = 0.020833
    n = len(sequence)

    if n < 10**6:
        return -1

    N = int(n / M)

    sequence = divide_str_to_str(sequence, N)

    L_values = []
    for L in sequence:
        L_values.append(BMA(L))

    n1 = M * 0.5
    n2 = (9 + (-1 ** (M + 1))) / 36
    n3 = (M / 3 + 2 / 9) / (2 ** M)  # doesn't work with M >= 2000
    mu = n1 + n2 - n3

    v_values = [0, 0, 0, 0, 0, 0, 0]

    K = len(v_values) - 1

    for Li in L_values:
        Ti = pow(-1, M) * (Li - mu) + (2/9)
        if Ti <= -2.5:
            v_values[0] += 1
        elif Ti <= -1.5:
            v_values[1] += 1
        elif Ti <= -0.5:
            v_values[2] += 1
        elif Ti <= 0.5:
            v_values[3] += 1
        elif Ti <= 1.5:
            v_values[4] +=1
        elif Ti <= 2.5:
            v_values[5] +=1
        elif Ti > 2.5:
            v_values[6] +=1


    X2obs = 0

    for i in range(len(v_values)):
        vi = v_values[i]
        pi = PI_VALUES[i]

        # im = ((vi - N * pi) ** 2) / (N * pi)

        X2obs += ((vi - N * pi) ** 2) / (N * pi)

    if debug:

        print(f"mu = {mu}")
        print(f'v_values = {v_values}')
        print(f'X2obs = {X2obs}')
        print()



    Pvalue = gammaincc(K/2, X2obs/2)

    return Pvalue




#

# sequence = generate_pseudo_random(10**6)
# print(sequence)

# with open("../sequence.txt", "r") as file:
#     sequence = file.readline()
#
# print(LinearComplexity(sequence))
# print(OverlappingTemplateMatching(input(), input(), int(input())))

# M: 1000
# mu = 500.22222222222223
# [10, 34, 145, 511, 229, 53, 18]
# 10 0.010417 0.016692809830085423
# 34 0.03125 0.242
# 145 0.125 3.2
# 511 0.5 0.242
# 229 0.25 1.764
# 53 0.0625 1.444
# 18 0.020833 0.3852488359813762
# 7.293941645811462
# 0.2945169662715907

# P = 0.44109483483802725