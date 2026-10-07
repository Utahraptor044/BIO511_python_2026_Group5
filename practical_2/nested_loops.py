sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']

"""
for sequence in sequences:
    for codon in codons:
        if codon in sequence:
            print(codon + " is in " + sequence)
"""

start_codons = ['ATG']
stop_codons = ['TAA','TAG','TGA']

list_of_sequences_with_both_codons = []
for sequence in sequences:
    for stop_codon in stop_codons:
        for start_codon in start_codons:
            if start_codon and stop_codon in sequence:
                list_of_sequences_with_both_codons.append(sequence)
print(f"Both a start and a stop-codon are found in {list_of_sequences_with_both_codons}")

if set(sequences) == set(list_of_sequences_with_both_codons):
    print(f"All {len(sequences)} sequences contain both start and stop codons.")

