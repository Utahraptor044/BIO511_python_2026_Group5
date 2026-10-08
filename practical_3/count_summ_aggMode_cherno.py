#Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

#Global variables

count = 999
summary = "unset"
result = "unset"

def count_above(seq,lim):
    count = 0

    for s in seq:           #For all s in the sequence
        if s > lim:         #If s > lim
            count += 1      #Increase count by 1
    return count            #Returns count and "stores" the variable 
 
print(count)                #Prints the global count variable
r = count_above(nums,limit) #Calling the function 'count_above'
print(r)                    #Prints the returned count variable as defined within the function ("local")
print(count)                #Prints the global count variable

"""
:::::::::::::::Output:::::::::::::::
999
2
999
:::::::::::::::Output:::::::::::::::
"""

def summarize_text(s):
    
    """
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    
    Summary:
    Function that classifies and enumerates characters in provided string
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::         
    """

    summary = {"digits":0,"letters":0,"other":0}    #Dictionary summary with keys - initialized values to 0 for all
    for char in s:
        if char.isdigit():                          #If character is a digit...
            summary["digits"] += 1                  #...Add +1 to the value of 'digits' key in 'summary' dictionary
        elif char.isalpha():                        #If character is a digit...
            summary["letters"] += 1                 #...Add +1 to the value of 'letters' key in 'summary' dictionary
        else:                                       #If character is something other than a digit or a letter...
            summary["other"] += 1                   #...Add +1 to the value of 'other' key in 'summary' dictionary
    return summary                                  #Returns the final state of the summary dictionary

print(summary)              #Prints summary as defined globally
sum = summarize_text(text)  #Calls the summarize function
print(sum)                  #Print summary as defined and as returned in the summarize function
print(summary)              #Prints summary as defined globally

print(len(text))            #Print length of text to confirm that the numbers add up

"""
:::::::::::::::Output:::::::::::::::
unset
{'digits': 5, 'letters': 21, 'other': 10}
unset
36
:::::::::::::::Output:::::::::::::::
"""

def aggregate(seq,mode,threshold):

    if mode == "sum":               #Variable result defined based on mode..
        result = 0
    elif mode == "count":
        result = 0
    elif mode == "max":
        result = None

    for n in seq:
        if n < 0:
            continue                        #Skips n if n < 0...that is, result remains unchanged
        if n >= threshold:
            if mode == "sum":               #Sum of all n values that are greater than threshold
                result = result + n         
            elif mode == "count":           #Counts number of n values that are greater than threshold
                result = result +1
            elif result == None or n > result:  #Max value n 
                result = n
    return result

print(result)

agg1 = aggregate(nums,"sum",limit)
print(agg1)

agg2 = aggregate(nums,"count",limit)
print(agg2)

agg3 = aggregate(nums,"max",limit)
print(agg3)

print(result)

"""
:::::::::::::::Output:::::::::::::::
unset
20
3
9
unset
:::::::::::::::Output:::::::::::::::
"""
agg4 = aggregate(nums,"max",100)
print(agg4)

"""
:::::::::::::::Output:::::::::::::::
None
:::::::::::::::Output:::::::::::::::
"""

# result = None due to "max" mode. There are no values n that are greater than the set threshold of 100
# so if-statement on line 80, 'if n >= threshold:' is never triggered. 'result' remains unchanged.

