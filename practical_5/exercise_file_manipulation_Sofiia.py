import csv
import sys
import numpy as np

#create a two-dimensional array that will become the 5x5 table
table = (np.arange(25).reshape(5,5))

usr_input = sys.argv[1]

#create a one-dimensional array that can be appended to the .csv file
new_row = (np.arange(5))

#writing two-dimensional array into a .csv file
with open("table_s.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(table)

#appending the one-dimensional array to .csv file based on user input
with open("table_s.csv", "a", newline = "") as file2:
    writer2 = csv.writer(file2)
    if str(usr_input) == 'yes' or str(usr_input) == 'y':
        writer2.writerow(new_row)
