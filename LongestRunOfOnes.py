#TESTED
from methods import *
from scipy.special import gammaincc




# from mpmath import gammaincc


def LongestRunOfOnes(sequence, M=None, K=None, N=None, PI_VALUES=None, debug=False):
    n = len(sequence)

    M8_PI_VALUES = {
        1: 0.2148,
        2: 0.3672,
        3: 0.2305,
        4: 0.1875
    }

    M128_PI_VALUES = {
        4: 0.1174,
        5: 0.2430,
        6: 0.2493,
        7: 0.1752,
        8: 0.1027,
        9: 0.1124
    }

    M1000_PI_VALUES = {
        10: 0.0882,
        11: 0.2092,
        12: 0.2483,
        13: 0.1933,
        14: 0.1208,
        15: 0.0675,
        16: 0.0727
    }

    if not M:
        if n >= 750000:
            M = 10000
            K = 6
            # N = 75
            PI_VALUES = M1000_PI_VALUES
        elif n >= 6272:
            M = 128
            K = 5
            # N = 49
            PI_VALUES = M128_PI_VALUES
        elif n >= 128:
            M = 8
            K = 3
            # N = 16
            PI_VALUES = M8_PI_VALUES
        else:
            print("To low sequence length")
            return -1

    # print(f"N: {N}   K: {K}")
    N = int(n / M)
    # print(N)
    sequence = divide_str_to_list(sequence, M)
    # print(sequence)
    #find the longest run of ones in each block
    longest_runs = []
    for block in sequence:
        block.append(0)
        longest_run = 1
        run = 1

        if block.count(1) == 0:
            longest_run = 0
        else:
            for i in range(M):
                if block[i] == 1 and block[i] == block[i+1]:
                    run += 1
                elif run != 0:
                    if longest_run < run:
                        longest_run = run
                        run = 1

        longest_runs.append(longest_run)


    # print(longest_runs)

    # count v values. vi = amount of runs = PIi value (longest_runs.count(PIi))
    v_values = []
    pi_keys = list(PI_VALUES.keys())
    # print(pi_keys)
    min_pi = min(pi_keys)
    max_pi = max(pi_keys)
    for pi in PI_VALUES.keys():
        vi = 0
        if pi == min_pi:
            for i in range(pi+1):
                vi += longest_runs.count(i)
        elif pi == max_pi:
            for i in range(pi, M+1):
                vi += longest_runs.count(i)
        else:
            vi = longest_runs.count(pi)

        v_values.append(vi)

    # print(v_values)

    X2obs = 0
    for i in range(K+1):
        pii = PI_VALUES[pi_keys[i]]

        n1 = (v_values[i] - (N * pii)) ** 2
        n2 = N * pii
        # print(n1, n2)
        X2obs += n1 / n2

        # X2obs += pow((v_values[i] - (N * pii)), 2.0) / (N * pii)

    # print(X2obs)

    if debug:
        print(f"X2obs = {X2obs}")
        print()

    Pvalue = gammaincc(K/2, X2obs/2)
    return Pvalue


# # 11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010 , P = 0.5007
# sequence = "1001010110000000101011110110011000110010101001111110100000010110111110001010101110110100110011101011000101000101000000000100111100111111010100111011111111111101110011010101110000000001101010011110101010101100100001111100010110010011100000000001111000111010110111111011011001111110100001101100101000000000010100100010110111000011101001111000101001110101000010000000001001101111101101101101111000101101001110011111100101100000000111000111000110100110011100001100100011110001111010100000000001001101101011111011000111101000011010011100110000010000000000110101110010111011001111000011101011100010000000111110000000001111101011001011110110101001100100101111100101010101000000000111110110011111110100111110001101000111100000110000000000000001100100111011101001011001011111111000111111000011110000000000010101011110111011110011100001110111010101110111110000000000000100101100101010000001001011000100100100100100001010000000000001011110000000001010101001110000110100000011101110001000000000011001000110100100"
# # sequence = generate_pseudo_random(10**3)
# print(sequence)
# print(f"P value: {LongestRunOfOnes(sequence)}")

#v = [34, 37, 28, 26]
#X2obs = 773.2874265591333
#P = 2.6880660240115117e-167