## Setup
# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

count = 999
summary = "unset"
result = "unset"

#Task1. Count numbers above a limit
print("Task1")

def count_above(seq, lim):
    count = 0
    for el in seq:
        if el>lim:
            count+=1
    return count

print("Global count is:", count)

task1_output = count_above(nums, limit)
print("Function count_above(nums, limit) returns:", task1_output)

print("Global count is:", count)
#Functions have their own namespaces and the variables within them do not overwrite global variables

#Task2. Summarise a text
#Write a function that classifies each character in a string as a digit, 
#a letter or something else.
print("Task2")

def summarize_text(s):
    summary = {"digits": 0, "letters": 0, "other":0}
    for char in s:
        if char.isdigit()==True:
           summary["digits"]+=1
        elif char.isalpha()==True:
            summary["letters"]+=1
        else:
            summary["other"]+=1
    return summary

print("Global summary is:", summary)

task2_output = summarize_text(text)
print("Function summarize_text(text) returns:", task2_output)

print("Global summary is:", summary)

#the function summarize_text counts all characters except for letters and numbers and records the number into "other". 
#in this case, "other" includes such symbols-- ":, &, ."

#Check that the numbers add up to the length of the string using len(text)
sum_values = 0
for value in summarize_text(text).values():
    sum_values+=value

if sum_values==len(text):
    print("The length of the string and the sum of values in the function output match.")
else:
    print("The length of the string and the sum of values in the function output are different.")

#Task3. Aggregate with a mode. Write one function that can calculate three different things,
#depending on a mode argument.
print("Task3")

def aggregate(seq, mode, threshold):
    result = 0
    if mode=="sum" or mode=="count":
        result = 0
    elif mode=="max":
        result = None
    for n in seq:
        if n < 0:
            continue
        elif n >= threshold:
            if mode=="sum":
                result+=n
            elif mode=="count":
                result+=1
            else:
                result=n
                #print(n)
    return result

print("Global result is:", result)

sum_result = aggregate(nums, "sum", limit)
print("Function aggregate(nums, 'sum', limit) returns:", sum_result)

count_result = aggregate(nums, "count", limit)
print("Function aggregate(nums, 'count', limit) returns:", count_result)

max_result = aggregate(nums, "max", limit)
print("Function aggregate(nums, 'max', limit) returns:", max_result)

print("Global result is:", result)

hund_result = aggregate(nums, "max", 100)
print("Function aggregate(nums, 'max', 100) returns:", hund_result)
#the threshold 100 is higher than all numbers in the input parameter nums, so
#no value in nums can fulfill the condition in the for loop inside the fucntion. 
#hence the function returns result = None, which was set earlier for all "max" mode operations.

#Task4. Errors and try/except
values = ['10', '5', ';', 'hello', '8', 'three', '2', '$#&^']

for el in values:
    try:
        print(int(el))
    except ValueError:
        print("Skipping invalid value:", el)
