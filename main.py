from generate_sequence import generate_sequence
from NIST_STS.Frequency import Frequency
from NIST_STS.BlockFrequency import BlockFrequency
from NIST_STS.Runs import Runs
from NIST_STS.LongestRunOfOnes import LongestRunOfOnes
from NIST_STS.Rank import Matrix
from NIST_STS.DiscreteFourierTransform import DiscreteFourierTransform
from NIST_STS.NonOverlappingTemplateMatching import NonOverlappingTemplateMatching
from NIST_STS.OverlappingTemplateMatching import OverlappingTemplateMatching
from NIST_STS.Universal import Universal
from NIST_STS.LinearComplexity import LinearComplexity
from NIST_STS.Serial import Serial
from NIST_STS.ApproximateEntropy import ApproximateEntropy
from NIST_STS.CumulativeSums import CumulativeSums
from NIST_STS.RandomExcursions import RandomExcursions
from NIST_STS.RandomExcursionsVariant import RandomExcursionsVariant
from NIST_STS.methods import *
from clock_generation import clock_generation

generation = input("blank - No generation ('ll be used previously generated sequence from the file sequence.txt)\n"
                   "0 - Clock generation\n"
                   "1 - Python pseudo random generation\n"
                   "Choose generation type: ")

if generation == "0":
    n = int(input("\nEnter len of sequence: "))
    clock_generation(n)
elif generation == "1":
    n = int(input("\nEnter len of sequence: "))
    sequence = generate_pseudo_random(n)
    with open("sequence.txt", "w") as file:
        file.write(sequence)

with open("./sequence.txt", "r") as file:
    sequence = file.readline()


debug = bool(input("Debug mode? (blank if not): "))

NIST_STS_tests = [
    "Frequency",
    "BlockFrequency",
    "Runs",
    "LongestRunOfOnes",
    "Rank (min len: 4 * 10**4)",
    "DiscreteFourierTransform (min len: 1000)",
    "NonOverlappingTemplateMatching",
    "OverlappingTemplateMatching (min len: 10**6)",
    "Universal (min len: 387840)",
    "LinearComplexity (min len: 10**6)",
    "Serial",
    "ApproximateEntropy",
    "RandomExcursions",
    "RandomExcursionsVariant (min len: 10**6)",
    "CumulativeSums (min len: 10**6)"
]

print()
for i in range(len(NIST_STS_tests)):
    print(f"{i}: {NIST_STS_tests[i]}")

len_sequence = len(sequence)
print(f"\nLen of sequence: {len(sequence)}")
tests = input("Select tests (blank if all): ")
if not tests:
    tests = [i for i in range(len(NIST_STS_tests))]
else:
    tests = [int(s) for s in tests.split()]
    tests.sort()
    tests = list(set(tests))
print()

NIST_STS_tests = [
    "Frequency",
    "BlockFrequency",
    "Runs",
    "LongestRunOfOnes",
    "Rank",
    "DiscreteFourierTransform",
    "NonOverlappingTemplateMatching",
    "OverlappingTemplateMatching",
    "Universal",
    "LinearComplexity",
    "Serial",
    "ApproximateEntropy",
    "RandomExcursions",
    "RandomExcursionsVariant",
    "CumulativeSums"
]
tests_copy = tests.copy()
for i in tests_copy:
    if NIST_STS_tests[i] == 'Rank' and len_sequence < 38*32*32:
        tests.remove(i)
    elif NIST_STS_tests[i] == 'DiscreteFourierTransform' and len_sequence < 1000:
        tests.remove(i)
    elif NIST_STS_tests[i] == 'OverlappingTemplateMatching' and len_sequence < 10 ** 6:
        tests.remove(i)
    elif NIST_STS_tests[i] == 'Universal' and len_sequence < 387840:
        tests.remove(i)
    elif NIST_STS_tests[i] == 'LinearComplexity' and len_sequence < 10 ** 6:
        tests.remove(i)
    elif NIST_STS_tests[i] == 'RandomExcursionsVariant' and len_sequence < 10 ** 6:
        tests.remove(i)
    elif NIST_STS_tests[i] == 'CumulativeSums' and len_sequence < 10 ** 6:
        tests.remove(i)

print(tests)

Pvalues = []
for i in tests:
    print(f"START {NIST_STS_tests[i].upper()}")

    if NIST_STS_tests[i] == 'Frequency':
        Pvalue = Frequency(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'BlockFrequency':
        Pvalue = BlockFrequency(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'Runs':
        Pvalue = Runs(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'LongestRunOfOnes':
        Pvalue = LongestRunOfOnes(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'Rank' and len_sequence >= 38*32*32:
        Pvalue = Matrix.binary_matrix_rank_text(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'DiscreteFourierTransform' and len_sequence >= 1000:
        Pvalue = DiscreteFourierTransform(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'NonOverlappingTemplateMatching':
        Pvalue = NonOverlappingTemplateMatching(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'OverlappingTemplateMatching' and len_sequence >= 10**6:
        Pvalue = OverlappingTemplateMatching(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'Universal' and len_sequence >=387840:
        Pvalue = Universal(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'LinearComplexity' and len_sequence >= 10**6:
        Pvalue = LinearComplexity(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'Serial':
        Pvalue = Serial(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'ApproximateEntropy':
        Pvalue = ApproximateEntropy(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'RandomExcursions' and len_sequence >= 10**6:
        Pvalue = RandomExcursions(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'RandomExcursionsVariant' and len_sequence >= 10**6:
        Pvalue = RandomExcursionsVariant(sequence, debug=debug)

    elif NIST_STS_tests[i] == 'CumulativeSums' and len_sequence >= 10**6:
        Pvalue = CumulativeSums(sequence, debug=debug)

    else:
        continue
    if str(Pvalue) == "nan":
        Pvalue = 0
    Pvalues.append(Pvalue)

print("\nTests completed!")
print("n:\t Pvalue")
for i in range(len(Pvalues)):
    Pvalue = Pvalues[i]
    print(f"{tests[i]} {NIST_STS_tests[tests[i]]}: {Pvalue}")

Psum = []
for P in Pvalues:
    if not type(P) == type([]):
        Psum.append(float(P))
    else:
        Psum.append(min(P))
        print(min(P))

average_P = sum(Psum) / len(Psum)
print(f"\nAverage P: {average_P}")

success = 0
for P in Pvalues:
    if not type(P) == type([]):
        success += P > 0.01
    else:
        s = 1
        for p in P:
            if not p > 0.01:
                s = 0
                break
        success += s

print(f'Len of sequence: {len_sequence}')
print(f"Successed test: {success};  "
      f"Failed test: {len(Pvalues) - success}")
if success == len(Pvalues):
    print("\nSequence is random")
else:
    print("\nSequence is not random :(")
