sequence_1 = "ATGCGTACTTAGCAAT"
sequence_2 = "TTAGGCATGCCGATATCGGCTTA"
sequence_3 = "ATGAATAACATGGATATTGTGAAAGCTGTAAAAGATGGAATGAAAAAGTCAGCCGACGCAACTTATTTAATGGATTTCAGGTCTGGTGCAAAAATAAACACTGAATATGTAGCTACCGTATCTATAGGTCTATCGTTGTTAGAAATAAAATCTTTTCGCCATGGTGATTACAAAGTTATATTTGAGTACCATACAAATAAATTCATTAATGCAACAGTTCCTTTATCGAAACGGTCTGATCCCCAAAAAATATTCTCAAAAAAAACTGTCAGAAAAAACACAAACACAACAAGATCAGGCAGAATTGATATTGCCATATTGGACAGCAGACCATTTTTCGACATTCCAATATGTGCAATAGAAGTTAAAGGAAATGCCCCCTGTAAAAGTCTTTTATTTTCTGACATAAGAAGAAATCTTGAATACTTTAAACACACAGGCCCTACAGGAAATTCAAGTCTTGGCCTAGCATTAAACTGTTCATTCCATTCATACAATGATTCAACTAAAAAAAATTACTGCACTACAATCCACCATAAGGAAGACATGATAAGGAAATTAAAAAACAAATATAAAAAATACATATCCGAATTAAATGAAGAAATTCCAGACGATATATCTGTTACAATTGATGTTTTTACAGCAGCAGAGCATTTACTATCTCCTGATGCTGACCAATATGAATACGAATCACATATAGATGACTTACATTTGACGCTTGGCGTTATGGTTATATTCGAACGAAAATCGATACTCAATTGA"

sequences = [sequence_1, sequence_2, sequence_3]

def gc_counter(s): 
    gc_count = 0
    for i in range(len(s)):
        if s[i] == 'G' or s[i] =='C':
            gc_count += 1
    return gc_count, len(s), (gc_count/len(s))*100

"""
for e in sequences:
    print("Total GC count in", e, f"is: {gc_counter(e)[0]}")
    print(f"Length of", e, f"is: {gc_counter(e)[1]}")
    print(f"GC percentage in", e, f"{gc_counter(e)[2]}")
    print('\n')
"""
"""
for j in range(len(sequences)):
    print(f"Total GC count in {sequences[j]} is {gc_counter(sequences[j])[0]}")
    print(f"Length of {sequences[j]} is {gc_counter(sequences[j])[1]}")
    print(f"GC percentage in {sequences[j]} is {gc_counter(sequences[j])[2]}")
"""

for j in range(len(sequences)):
    print("===================================")
    print(f"For sequence_{j+1}:")
    print(f"Total GC count is: {gc_counter(sequences[j])[0]}")
    print(f"Length is: {gc_counter(sequences[j])[1]} bp")
    print(f"GC percentage is: {gc_counter(sequences[j])[2]}")
