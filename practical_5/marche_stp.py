# recover the CSV file
# Print it
# Transform it into a pandas dataframe

print("begin")

import csv
import pandas as pd
import argparse
# import sys

parser = argparse.ArgumentParser(description="Read a csv file and print its statistics")

# Demande de récupérer le script convoité
parser.add_argument('file', help="Choose a csv file to analyse, as louis.csv for example")

# Encode its value
args = parser.parse_args()

# Be careful, use the right name
with open(args.file, "r", newline ='', encoding='latin-1') as file:
    reader = csv.reader(file, delimiter = ",")
    # create a variable that recover all of the data
    data = list(reader)



df = pd.DataFrame(data).apply(pd.to_numeric, errors="coerce")
#pd.to_numeric try to convert each value into an int

print("Contenu du fichier :")
print(df)

print("\nRésumé statistique :")
print(df.describe())

#print("Contenu du fichier :")

# .to_string() print the entire dataframe
#print(df)
#print(df.describe())