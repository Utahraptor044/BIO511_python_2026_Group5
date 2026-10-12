#Exercise 1: Count numbers above a limit


# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

def count_above (seq, lim):
    count = 0
    for num in seq:
        if num > lim:
            count += 1
    return count

print ("Count of numbers above limit:", count_above(nums, limit))

#Answer: The global count is still 999 because the function 
# uses a local varible that is separate from the global one.

#Exercise 2: Summarize text

def summarize_text (s):
    summary = {
        "digits": 0,
        "letters": 0,
        "others": 0,
    }
    for char in s:
        if char.isdigit():
            summary["digits"] += 1
        elif char.isalpha():
            summary["letters"] += 1
        else:
            summary["others"] += 1
    return summary

print ("Summary of text:", summarize_text(text))
print ("Length of text:", len(text))
print ("Number of digits:", summarize_text(text)["digits"])

#Answer: "others" counts as spaces and punctuation.

#Check that the numbers add up to the length of the string using len(text).

#Exercise 3: Aggregate with a mode

def aggregate (seq, mode, threshold):
    result = []
    if mode == "sum":
        result = 0
    if mode == "count":
        result = 0
    if mode == "max":
        result = None

    for n in seq:
        if n < 0:
            continue
        elif n < threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result is None or n > result:
                    result = n
    return result

print ("Result:",result)
aggregate (nums, "sum", limit)
print ("Result:",result)
aggregate (nums, "count", limit)
print ("Result:",result)
aggregate (nums, "max", limit)
print ("Result:",result)

#Answer: aggregate(nums, "max", 100) returns the maximum number
#in the list that is less than 100, 9.

#Exercise 4:

values = ['10', '5', 'hello', 'Joy','8', 'three', '2']

for i in values:
    try:
        num = int(i)
        print (num)
    except ValueError:
        print ("Skipping invalid value:", i)
        continue


    


