list = ["Prayest of the Refugees", "The emptiness machine", "Help myself", "Mr Mme", "Une vie à t'aimer", "We shall sail together", "Leave it all behind"]

index=0
type(list)

for song in list:
    index+=1
    if index >= 2:
        break
    print(index, "ème musique: ", song)

sequence = 'GATTACAGAACTGATAC'

# Have to find the third A

a_cnt = 0
cnt_while = 0

askedA = int(input("Print the position of the wanted adenosine. Type a number: \n"))
while True:
    nucleo = sequence[cnt_while]
    if nucleo == 'A' or nucleo == 'a': 
        a_cnt+=1
    cnt_while+=1
    if a_cnt == askedA:
        print("The third adenosine is at the", cnt_while, "th position")
        break
    if cnt_while == len(sequence):
        print("There is less than", askedA, "adenosine in this sequence")
        print("Check the position of the stop in case of problems by printing the last nucleotide:", sequence[cnt_while-1])
        break


# Find the nucleodide position with a for loop
forA_cnt = 0
cnt_position_for = 1
for nucleo in sequence:
    if nucleo == 'A' or nucleo == 'a': 
        forA_cnt+=1
    if forA_cnt == askedA:
        print("The third adenosine is at the", cnt_position_for, "th position")
        break
    cnt_position_for += 1


##################################################################################################
## Looking for stop and start codons ##

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']

start_codon = ["ATG"]
stop_codons = ["TAA", "TAG", "TGA"]

# Have to check if sequences have both start and stop codons
for sequence in sequences:
    # Remember if there is a start codon in the current sequence
    start_p = False
    stop_post_start = False
    stop_before_start = False
    only_stop = False
    i = 0
    # Check for every groups of 3 nucleotides
    for n in sequence:
        # If the trio of nucleotide is no more in the sequence, break this loop
        if i+2 > len(sequence) and start_p == False:
            #print("No start codon found in the sequence", sequence)
            continue
        
        # Create the trio to analyse
        analyse = sequence[i:i+3]

        # Check if the start codon is the current trio
        for start in start_codon:
            if analyse == start:
                # If there is a start codon, cut the begin of the sequence and register the information
                seq_cut = sequence[i+3:]
                start_p = True

        # Break the sequence reading  
        if start_p == True:
            break

        i+=1
    if start_p == True:
        for stop in stop_codons:
            if stop in seq_cut:
                stop_post_start = True
            elif stop in sequence[:i+3]:
                stop_before_start = True

    if start_p == False:
        for codon in stop_codons:
            if stop in sequence:
                only_stop = True

    # Get the answer messages
    if start_p == True and stop_post_start == False and stop_before_start == False and only_stop == False:
        print("There is only a start codon in the sequence:", sequence)
    elif start_p ==True and stop_post_start == True and stop_before_start == True:
        print("There is stop codon before and after the start codon in the sequence:", sequence)
    elif start_p == True and stop_post_start == True and stop_before_start == False:
        print("There is a stop codon after the start codon in the sequence:", sequence)
    elif start_p == True and stop_post_start == False and stop_before_start == True:
        print("There is a stop codon before the start codon in the sequence:", sequence)
    elif only_stop == True:
        print("There is only a stop codon in the sequence:", sequence)
    elif start_p == False and only_stop == False:
        print("There is no start or stop codon in the sequence", sequence) 
    else:
        print("There is an error for the case of the sequence :", sequence)

            
                

#print("There is a start codon before a stop codon in the sequence:", sequence)


###########################################################################################
### Reverse the dictionnary ###

# Data

data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# Create a list to register all of the known strands
unique_bacteria = []

###
# First, will register all of the identified strands

for ID, bact_strain in data.items():
    for strain in bact_strain:
        if not strain in unique_bacteria:
            unique_bacteria.append(strain)

print("list of the refereced bacterial strands :", unique_bacteria)

###
# Link each bacterial stand to the patients

# Create the dictionary

bacteria_to_patient = {}

for strand in unique_bacteria:
    #print(strand)
    bacteria_to_patient[strand]="[]"

print("New dictionary created:", bacteria_to_patient)

# Check for every patient if they have the strand. If yes, append their ID to the right bacterial strand

for strand, patient in bacteria_to_patient.items():
    result_ID = []
    for ID, bact_str in data.items():
        if strand in bact_str:
            #print(strand)
            result_ID.append(ID)
    bacteria_to_patient[strand] = result_ID
            
            
print(bacteria_to_patient)
    

