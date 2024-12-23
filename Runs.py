#TESTED
from scipy.special import erfc
from math import sqrt
from methods import *
def Runs(sequence, debug=False):
    if debug:
        print("Runs")
    n = len(sequence)


    sequence = convert_to_list(sequence)
    j = sum(sequence) # sum of ones
    pi = j / n

    # tau = 2 / sqrt(n)
    tau = 2 / n

    if abs(pi - 0.5) <= tau:
        if debug:
            print(f"pi = {pi}")
            print(f"tau = {tau}")
        return 0

    Vn_obs = 1
    for i in range(n-1):
        if sequence[i] != sequence[i+1]:
            Vn_obs += 1

    if debug:
        print(f"pi = {pi}")
        print(f"tau = {tau}")
        print(f"vn_obs")
        print()

    try:
        Pvalue = erfc(abs(Vn_obs - 2 * n * pi * (1 - pi))/(2*sqrt(2 * n) * pi * (1 - pi)))
    except:
        Pvalue = 0

    return Pvalue

# 1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000 , P = 0.5007
# sequence = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
# sequence = generate_pseudo_random(10**3)
# print(sequence)
# print(Runs(sequence))