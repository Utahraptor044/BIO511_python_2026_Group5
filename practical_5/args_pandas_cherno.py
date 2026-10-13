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
info = pd.DataFrame.info(dframe)
print(info)

""" :::::::::::::::Output:::::::::::::::
(envy) chomar@GottMos:~/BIO511_python_2026_Group5/practical_5$ python args_pandas_cherno.py --input dataset.csv 
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['11', '12', '13', '14', '15']
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   1       5 non-null      int64
 1   2       5 non-null      int64
 2   3       5 non-null      int64
 3   4       5 non-null      int64
 4   5       5 non-null      int64
dtypes: int64(5)
memory usage: 332.0 bytes
None
:::::::::::::::Output::::::::::::::: """