sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
#codons = ['CCA', 'TGT', 'GTA', 'TAG']

"""
for sequence in sequences:
    for codon in codons:
        if codon in sequence:
            print(codon + " is in " + sequence)
"""
#=========================================================================================

"""
start_codons = ['ATG']
stop_codons = ['TAA','TAG','TGA']

list_of_sequences_with_both_codons = []
for sequence in sequences:
    for stop_codon in stop_codons:
        if ('ATG' and stop_codon) in sequence:
            list_of_sequences_with_both_codons.append(sequence)
print(f"Both a start and a stop-codon are found in {list_of_sequences_with_both_codons}")

if set(sequences) == set(list_of_sequences_with_both_codons):
    print(f"All {len(sequences)} sequences contain both start and stop codons.")
"""
#=========================================================================================

start_codons = ['ATG']
stop_codons = ['TAA','TAG','TGA']

list_of_sequences_with_start_codons_before_stop_codons = []
list_of_sequences_with_stop_codons_before_start_codons = []
sequence_start_codon_pos = {}
sequence_stop_codon_pos = {}


for sequence in sequences:
    for start_codon in start_codons:
        for i in range(len(sequence)):
            if start_codon == sequence[i:i+3]:
                #print(f"start codon {start_codon} found in sequence {sequence} starting at {i} ending at {i+3}")
                #print(f"in sequence {sequence} the start codon has position {i}")
                sequence_start_codon_pos[sequence] = i

    for stop_codon in stop_codons:
        for i in range(len(sequence)):
            if stop_codon == sequence[i:i+3]:
                #print(f"stop codon {start_codon} found in sequence {sequence} starting at {i} ending at {i+3}")
                #print(f"in sequence {sequence} the stop codon has position {i}")
                sequence_stop_codon_pos[sequence] = i

print("start", sequence_start_codon_pos)
print("stop", sequence_stop_codon_pos)

for i,j in sequence_start_codon_pos.items():
    for k,l in sequence_stop_codon_pos.items():
        if i == k and j < l:
            list_of_sequences_with_start_codons_before_stop_codons.append(i)
        if i == k and j > l:
            list_of_sequences_with_stop_codons_before_start_codons.append(i)
            
print(f"{len(list_of_sequences_with_start_codons_before_stop_codons)} sequences with start codons before stop codons: {list_of_sequences_with_start_codons_before_stop_codons}")
print(f"{len(list_of_sequences_with_stop_codons_before_start_codons)} sequences with stop codons before start codons: {list_of_sequences_with_stop_codons_before_start_codons}")