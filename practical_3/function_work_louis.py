def add_numbers(number_one, number_two):
    result = number_one + number_two
    return result

print(add_numbers(5, 6))

#############################################################################################"

# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

# Create a function that count the number of values that are greater than a defined limit. 

def count_above(seq, lim=8):
    count = 0
    great_val = []
    for value in seq:
        if value > lim:
            count +=1
            great_val.append(value)

    return count, great_val

print(count_above(nums, limit))
print(count)

########################################################################################
# Summarising a text

def summarize_text(s):
    summary = {"digits": 0, "letters": 0, "other": 0}
    for character in s:
        if character.isdigit() == True:
            summary["digits"]+=1
        elif character.isalpha() == True:
            summary["letters"]+=1
        else :
            summary["other"]+=1
    summary["Nubmer of characters"] = len(s)
    return summary

print(summarize_text(text))

#################################################################################################
### Agregate function ###

def agregate(seq, mode, threshold):

    # define the sum mode
    if mode == "sum" :
        result = 0
        for value in seq :

            # check for every value the condition of use
            if value > 0 and value >= threshold:
                result += value
            else:
                print("error block sum")

    # define the count mode
    elif mode == "count" :
        result = 0
        for value in seq:

            # Check the condition of use and count the number of value that pass the if statement
            if value > 0 and value >= threshold:
                result += 1
            else:
                print("Error block count")

    # Define the max mode
    elif mode == "max" :
        result = None
        for value in seq:
            # Find a first value that can replace the none value
            if (value > 0 and value >= threshold) and  result == None :
                result = value

            # Look if the current value is greater than the previous registered one
            elif (value > 0 and value >= threshold) and  value > result :
                result = value
    
    # In case of error in the mode selection
    else :

        result= "Please choose a mode between 'sum', 'count' and 'max'"

    return result

print(agregate(nums, "max", 3))

