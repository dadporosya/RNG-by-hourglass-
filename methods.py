from random import random, Random
from numpy import zeros as zeros
from copy import copy as copy
from numpy import dot as dot

def plus_minus(string):
    plus_minus = []
    for i in string:
        i = int(i)
        if i == 0:
            i = -1
        plus_minus.append(i)
    return plus_minus

def divide_str_to_list(string, M):
    """Divide string into M lists"""
    divided_str = [[]]
    index = 0
    M_counter = 0
    for s in string:
        divided_str[index].append(int(s))
        M_counter += 1
        if M_counter == M:
            index += 1
            M_counter = 0
            divided_str.append([])

    if len(divided_str[-1]) < M:
        divided_str.pop(-1)

    return divided_str


def divide_str_to_str(string, M):
    """Divide string into M strings"""
    divided_str = [""]
    index = 0
    M_counter = 0
    for s in string:
        divided_str[index] += s
        M_counter += 1
        if M_counter == M:
            index += 1
            M_counter = 0
            divided_str.append("")

    if len(divided_str[-1]) < M:
        divided_str.pop(-1)

    return divided_str


def divide_in_2_segments(string, L, Q):
    """Divide string into 2 segments Q and K strings. L - len of each block"""
    divided_str = [""]
    index = 0
    L_counter = 0
    for s in string:
        divided_str[index] += s
        L_counter += 1
        if L_counter == L:
            index += 1
            L_counter = 0
            divided_str.append("")

    if len(divided_str[-1]) < L:
        divided_str.pop(-1)

    Q_segment = divided_str[0:Q]
    K_segment = divided_str[Q:len(divided_str)]

    return Q_segment, K_segment


def convert_to_list(string):
    """Convert string to list with int elements"""
    list = []
    for s in string:
        list.append(int(s))
    return list

def convert_to_list_str(string):
    """Convert string to list with str elements"""
    list = []
    for s in string:
        list.append(s)
    return list

def generate_pseudo_random(n):
    """Generate pseudo random sequence with n length"""
    sequence = ""
    while len(sequence) < n:
        r = random()
        r = int(r * (10 ** (len(str(r)) + 1)))
        binary = bin(r)[2:-1]
        sequence += binary

    sequence = sequence[0:n]
    return sequence

def all_possible_variants(n):
    """n - len of binary string"""
    variants = ["0"*n]
    i = 0
    while i < 2**n:
        # print(variants[i])
        start_string = convert_to_list_str(variants[i])
        for j in range(n):
            test_string = start_string[0:n]
            test_string[j] = "1"
            test_string = "".join(test_string)
            if not test_string in variants:
                variants.append(test_string)
            # print(test_string)
        i += 1
        # print(variants)

    return variants

# def BMA(sequence):
#     n = len(sequence)
#     # C = B = [0]*500
#     C = B = [0] * n
#
#     C[0] = B[0] = 1
#     L = 0
#     m = -1
#     i = 0
#
#     while i < n:  # Iterating over the input sequence
#         Delta = 0
#         for p in range(0, L + 1):
#             Delta = Delta + C[p] * int(sequence[i - p])
#         if (Delta % 2) == 1:
#             if C[i - m] == 0:
#                 C[i - m] = 1
#             else:
#                 C[i - m] = 0
#             if L <= i // 2:
#                 m = i
#                 L = i + 1 - L
#         i = i + 1
#
#     return L

def BMA(block_data):
    n = len(block_data)
    c = zeros(n)
    b = zeros(n)
    c[0], b[0] = 1, 1
    l, m, i = 0, -1, 0
    int_data = [int(el) for el in block_data]
    while i < n:
        v = int_data[(i - l):i]
        v = v[::-1]
        cc = c[1:l + 1]
        d = (int_data[i] + dot(v, cc)) % 2
        if d == 1:
            temp = copy(c)
            p = zeros(n)
            for j in range(0, l):
                if b[j] == 1:
                    p[j + i - m] = 1
            c = (c + p) % 2
            if l <= 0.5 * i:
                l = i + 1 - l
                m = i
                b = temp
        i += 1
    return l

    # print(str(bin))
#
# print(divide_str('10101011111110101010101', 4))

def convert_seeds_to_bin(seeds, bin_pow=1, generator=None):
    print(generator)
    bin_sequence = ""
    if generator == "C++":
        a = 48271
        c = 0
        m = 2 ** 31 - 1
    for seed in seeds:
        if not generator:
            if bin_pow < 0 and seed == 0:
                binary += "0"
                continue
            word = seed ** bin_pow

            if bin_pow < 0 or str(type(bin_pow)) == "<class 'float'>":
                e = 0
                for i in range(len(str(word))):
                    if str(word)[i] == "e":
                        e = int(str(word)[i + 2:])
                word *= 10 ** e
                word = int(str(word).replace('.', ''))
        elif generator == "C++":
            word = (a * seed + c) % m
        elif generator == "python":
            word = Random(seed).random()
            word = int(str(word)[2:])


        binary = bin(word)[2:-1]
        bin_sequence += binary
    return bin_sequence