
# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

def aggregate(seq,mode,threshold):
    if mode == "sum":
        result = 0
        for n in seq:
            if n < 0:
                continue
            if n >= threshold:
                result += n


    if mode == "count":
        result = 0
        for n in seq:
            if n < 0:
                continue
            if n >= threshold:
                result += 1

    if mode == "max":
        result = None
        for n in seq:
            if n < 0:
                continue
            try:
                if n > result:
                    result = n
            except TypeError:
                    result = n
    return result

print("global result:", result)
print(aggregate(nums, "sum", limit))
print(aggregate(nums, "count", limit))
print(aggregate(nums, "max", limit))
print("global result:", result)

"""
        Print the global result. # global result:unset
        Call the function three times and print each returned value:
            aggregate(nums, "sum", limit) # 20
            aggregate(nums, "count", limit) # 3
            aggregate(nums, "max", limit) # Type Error on line 35: TypeError: '>' not supported between instances of int and NonType
        Print the global result again. # It won't print because of the Error that was triggered when command on line 42 tried to execute
"""
# Q: What does aggregate(nums, "max", 100) return, and why?
# A: TypeError, like the one for aggregate(nums, "max", limit) that is due to line 35:  int > None

print("Q:", aggregate(nums, "max", 100))

# After addition of Error handling
# 
