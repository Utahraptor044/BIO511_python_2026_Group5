
# bacteria_to_patients

data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

#Collect the unique bacteria - Generate list of unique bacteria.
unique_bacteria = []
for bact_list in data.values():
    for bacterium in bact_list:
        if bacterium not in unique_bacteria:
            unique_bacteria.append(bacterium)
#print(unique_bacteria)

#Create the reverse dictionary.
bacteria_to_patients = {}
for bacterium in unique_bacteria:
    bacteria_to_patients[bacterium] = [] #creates a dictionary with bacterial strains as keys; each with an empty list as value
#print(bacteria_to_patients)

for pat, bact_list in data.items(): #Loops through each item in the dictionary, naming the key, pat and the value, bact_list
    for strain in bact_list:
        if strain in bacteria_to_patients.keys():
            bacteria_to_patients[strain].append(pat) #appends the patient (pat) to the value of each bacteria-key
print(bacteria_to_patients)