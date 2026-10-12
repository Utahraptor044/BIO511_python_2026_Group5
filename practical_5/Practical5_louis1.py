import csv
import sys

# Add a protection to be sure that the user add 5 values
if len(sys.argv) != 6:
    print("Please enter 5 values to add to the file")
    sys.exit(1)

#original_file = sys.argv[1]
add_line = sys.argv[1:]
print(type(add_line))
print(add_line)

# First, fill the csv file with known data (provided by ChatGPT)

with open("louis.csv", "w", newline="", encoding="latin-1") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerows([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ])

# Add the new line

with open("louis.csv", "a", newline = '', encoding='latin-1') as file:
    # add lines in the file
    writer = csv.writer(file, delimiter = ",")
    writer.writerow(add_line)

# Notified that the file is ready
print("The csv file is created and filled")


#with open("louis.csv", "r", newline = '', encoding='latin-1') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(row)

    



         

