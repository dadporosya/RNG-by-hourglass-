from NIST_STS.methods import *


def generate_sequence(n):
    sequence = generate_pseudo_random(5000)
    with open("sequence.txt", "w") as file:
        file.write(sequence)

# generate_sequence(6)