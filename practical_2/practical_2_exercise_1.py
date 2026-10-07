unique_bacteria = []

data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

for pat,bact in data.items():
    for strain in bact:
        if strain not in unique_bacteria:
            unique_bacteria.append(strain)
print(unique_bacteria)