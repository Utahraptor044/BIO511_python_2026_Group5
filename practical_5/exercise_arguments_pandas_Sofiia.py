import os
import argparse
import csv
import numpy as np
import pandas as pd

#checking if the input file exists
def existing_file(file_path):
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', type=existing_file, required=True,  help='Path to the input .csv file')
    args = parser.parse_args()

    #reading the input file
    with open(args.table, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        dict1={}
        i = 0
        #making a dictionary with row numbers as keys and rows as values
        for row in reader:
            i+=1
            dict1[i]=row

        #creating a pandas dataframe from a dictionary
        df = pd.DataFrame(dict1)

        #created dataframe is transposed compared to the input csv file, so transposing it back
        df_t = df.T

        print("Dataframe:\n", df_t)
        print("Statistic summary of dataframe with describe():\n", df_t.describe())
    

if __name__ == "__main__":
    main()
