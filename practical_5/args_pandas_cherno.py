import argparse,csv, pandas as pd

parser = argparse.ArgumentParser()
frame = []

parser.add_argument('--input', help='Specify the name of the input file')

args = parser.parse_args()

with open(f'{args.input}','r') as file:     #Opens and reads the file from --input (should be dataset.csv). dataset.csv was created by filemanip_cherno.py
    reader = csv.reader(file,delimiter=',') #csv.reader reads 
    writer = csv.writer(file)
    for row in reader:                      #For each row read by reader
        print(row)                          #Prints row

dframe = pd.read_csv(args.input)
info = pd.DataFrame.describe(dframe)
print(info)

""" :::::::::::::::Output:::::::::::::::
(envy) chomar@GottMos:~/BIO511_python_2026_Group5/practical_5$ python args_pandas_cherno.py --input dataset.csv 
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['11', '12', '13', '14', '15']
               1          2          3          4          5
count   5.000000   5.000000   5.000000   5.000000   5.000000
mean    3.000000   4.000000   5.000000   6.000000   7.000000
std     4.472136   4.472136   4.472136   4.472136   4.472136
min     1.000000   2.000000   3.000000   4.000000   5.000000
25%     1.000000   2.000000   3.000000   4.000000   5.000000
50%     1.000000   2.000000   3.000000   4.000000   5.000000
75%     1.000000   2.000000   3.000000   4.000000   5.000000
max    11.000000  12.000000  13.000000  14.000000  15.000000
:::::::::::::::Output::::::::::::::: """