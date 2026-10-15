# Simple loops
sequence = 'GATTACAGAACTGATAC'

list = ['a','b',3,5,6,8,9]

iteration = 0
for i in list:
    print(i)
    iteration += 1
    if iteration > 4:
        break

# While loops

sequence = 'GATTACAGAACTGATAC'

print("Using a_count = 0 :::")

#1 Use a while loop

a_count = 0
position = 0

while a_count < 3 and position < len(sequence):
    if sequence[position] == "A":
        a_count += 1
    position += 1

print(f"Using while-loop: The position of 3rd base A in the sequence is: {position}")

#2 Use a for loop

a_count = 0
position = 0

for base in sequence:
    if sequence[position] == "A":
        a_count += 1
    if a_count == 3:
        break
    position += 1
print(f"Using for-loop: the position of the 3rd base A in the sequence is {position+1}")

#4 with the count_a variable
print("Using count_a = 3 :::")

#1 Use a while loop

count_a = 3
position = 0

while count_a < 10 and position < len(sequence):
    if sequence[position] == "A":
        count_a += 1
    position += 1

print(f"Using while-loop: The position of 10th base A (after first having found 3 As) in the sequence is: {position}")

#2 Use a for loop

count_a = 3
position = 0


for base in sequence:
    if sequence[position] == "A":
        count_a += 1
    if count_a == 10:
        break
    position += 1
print(f"Using for-loop: the position of the 10th base A (after first having found 3 As) in the sequence is {position+1}")

#Nested Loops

#2

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']

start = ['ATC']

stop = ['TAA','TAG','TGA']

sta_seq = [] #Empty list - Reserved for sequences that have start codons
sto_seq = [] #Empty list - Reserved for sequences that have stop codons

for sequence in sequences:
    for sta in start:
        if sta in sequence:
            print(sequence + " has start codon")
            sta_seq.append(sequence)         #Appends sequences with start codons to sta_seq list
    for sto in stop:
        if sto in sequence:
            print(sequence + " has stop codon")
            sto_seq.append(sequence)         #Appends sequences with stop codons to sto_seq list


print(sta_seq) #Prints list of sequences that have start codons
print(sto_seq) #Prints list of sequences that have stop codons

both = set(sta_seq) & set(sto_seq)  #Creates a set of shared values (intersection) between the lists sta_seq and sto_seq, first by converting the lists into sets. 
                                    #Sets can only have unique values. I.e. sequences that have both start and stop codons will be in both sets.
                     
print("sequences " + str(both) + " have start and stop codons") #Prints the sequences, from the set both, having both start and stop codons

#3

for sequence in sequences:                                      #Loops through sequences
    for sta in start:                                           #Loops through start codons    
        if sta in sequence and sequence.index(sta)%3 == 0:      #If the start codon is in the sequence and its index position is divisible by 3...it is a start codon
            print(f"the start codon {sta} is in sequence {sequence} at position {sequence.index(sta)}") #Prints start codon, sequence and position of start codon within the sequence
            for sto in stop:                                    #Loops through stop codons 
                if sto in sequence and (sequence.index(sto))%3 == 0:    #If the stop codon is in the sequence and its index position is divisible by 3...it is a stop codon
                    print(f"the stop codon {sto} is in sequence {sequence} at position {sequence.index(sto)}") #Prints stop codon, sequence and position of stop codon within the sequence
                    if sequence.index(sto) > sequence.index(sta):                       #Filters that the stop codon is further downstream (higher position) than the start codon - Proper sequence.
                        print(f"sequence {sequence} is a legit sequence with start codon at position {sequence.index(sta)} and stop codon at position {sequence.index(sto)}")