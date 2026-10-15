data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

""" # Loop through the dict printing each key and each value as a list.
for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)
  print('bac889Ytd' in value_bact_list) """

unique_bacteria = []

for bacteria_list in data.values():
    for bacteria in bacteria_list:
       if bacteria not in unique_bacteria:
        unique_bacteria.append(bacteria)

print(unique_bacteria)

bacteria_to_patients = {}

for u_bact in unique_bacteria:
    if u_bact not in bacteria_to_patients.keys():
        bacteria_to_patients[u_bact] = []

print(bacteria_to_patients)

for patients in data.keys():
    for bacteria in data[patients]:
        bacteria_to_patients[bacteria].append(patients)
        
print(bacteria_to_patients)
