import sys, csv

data = ['1','2','3','4','5']                        #Creating 5 column list of data

with open('dataset.csv','w',newline='') as table:   #Creates file dataset.csv
    
    firstrow = csv.writer(table, delimiter=',')
    firstrow.writerow(data)                         #Creates first row in table. Populated with data as defined above.
    rows = 1                                        #First row has been created, so rows = 1
    while rows < 5:                                 #We want 5 rows - While loops Adding rows until rows = 5 
        firstrow.writerow(data)              
        rows += 1   

arg1 = sys.argv[1]                                  #Input Arguments 1-5 defined
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]
arg5 = sys.argv[5]

with open('dataset.csv','a') as appendix:
    appendix.write(arg1+"," + arg2+"," + arg3+"," + arg4+"," + arg5 + "\n") #Appends a row to the file based on the user's input using argv

