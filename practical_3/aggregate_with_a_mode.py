def aggregate(seq, mode, threshold):

#########################################################################################"
# require data #

nums = [3, -1, 7, 2, 9, 0, 4]


# Louis' version    
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

