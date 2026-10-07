#Task1. Simple loops
#1)Create a list of 7 items. Loop over the list printing each item of the list.
mustelidae = ("polecats", "badgers", "martens", "weasels","sables", "ermines", "grisons")

print("Task1.1")
for el in mustelidae:
    print(el)

#2)For each iteration, print the loop number (index).
print("Task1.2")
i=1
for el in mustelidae:
    print(i, el)
    i+=1

#3)Add an If-statement to make the loop stop after printing its 5th item
print("Task1.3")
i=1
for el in mustelidae:
    print(i, el)
    i+=1
    if i>5:
        break


#Task 2. While loops
sequence = 'GATTACAGAACTGATAC'
#1) Use a while loop.
print("Task2.1")

while_a_counter=0
seq_index=0

while while_a_counter < 3:
    if sequence[seq_index]=="A":
        while_a_counter+=1
    seq_index+=1
print(seq_index-1)

#2) Use a for loop.
print("Task2.2")
for_a_counter=0

for index, character in enumerate(sequence):
    if character=="A":
        for_a_counter+=1
    if for_a_counter==3:
        break
print(index)

#3) Print the position of the third A for both solutions.
print("Task2.3")
print("Position of third A using while loop:", seq_index-1)
print("Position of third A using for loop:", index)

#4) Use count_a = 3 
print("Task2.4")
count_a = 3

#while loop
while_a_counter=0
seq_index=0

while while_a_counter < count_a:
    if sequence[seq_index]=="A":
        while_a_counter+=1
    seq_index+=1

print(f"Position of {count_a} A using while loop:", seq_index-1)


#for loop
for_a_counter = 0

for index, character in enumerate(sequence):
    if character=="A":
        for_a_counter+=1
    if for_a_counter >= count_a:
        break

print(f"Position of {count_a} A using for loop:", index)

print("What happens if you look for the tenth A in the sequence? IndexError: string index out of range")

#Task3. Nested loops
#1) See if you can follow every line and work out how this example code works.
# The code iterates over each sequence in the sequences list. For each sequence
# it goes over every codon in the codons list and searches whether each codon 
# is present in the sequence. If it is present-- the codon and sequence it is found in are printed out.

#2)Create a nested for loop as in the example which looks for start and stop codons in the sequences
# list from the example above. Which sequences have both a start and a stop codon?
print("Task3.2")

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
start_codon = "ATG"
stop_codons = ['TAA', 'TAG', 'TGA']
sequences_with_start_and_end = []

#Which sequences have both a start and a stop codon?
for sequence in sequences:
    for stop_codon in stop_codons:
        if start_codon and stop_codon in sequence:
            print("Sequence ", sequence, "has start codon", start_codon, "and stop codon", stop_codon)
            sequences_with_start_and_end.append(sequence)
print("Sequences with both start and stop codons:", set(sequences_with_start_and_end))

#3)Try to find a way to make sure that the start codon is before the stop codon in a sequence.
# Which sequence(s) have a start codon before a stop codon?
print("Task3.3")

seq_with_start_before_stop=[]

for sequence in set(sequences_with_start_and_end):
    for stop_codon in stop_codons:
        if start_codon and stop_codon in sequence:
            start_position = len(sequence.split(start_codon)[0]) + 1
            stop_position = len(sequence.split(stop_codon)[0]) + 1
            if start_position < stop_position:
                print("Sequence", sequence, "has start codon ATG before stop codon at", start_position, "and stop codon", stop_codon, "at", stop_position)
                seq_with_start_before_stop.append(sequence)
print("Sequences that have a start codon before a stop codon:", set(seq_with_start_before_stop))

#Task4. Loop through a dictionary
data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}
#1)Collect the unique bacteria.
print("Task4.1")

unique_bacteria = []

for key_patient, value_bact_list in data.items():
    for bact in value_bact_list:
        if bact not in unique_bacteria:
            unique_bacteria.append(bact)

print("Unique bacteria:", unique_bacteria)

#2)Create the reverse dictionary
print("Task4.2")

bacteria_to_patients = {}

for el in unique_bacteria:
    if el not in bacteria_to_patients:
        bacteria_to_patients[el] = []

print("Dictionary with empty lists as values:", bacteria_to_patients)

#3)Add the patients to the reverse dictionary.
print("Task4.3")

for keys, values in data.items():
        for val in values:
            bacteria_to_patients[val].append(keys)

print("Reversed dictionary:", bacteria_to_patients)
