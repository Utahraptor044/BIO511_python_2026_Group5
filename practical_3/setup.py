# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

def count_above(seq, lim):
    count = 0
    for i in range(len(seq)):
        if i > lim:
            count += 1
    return count

print(f"The global: {count}")

print(f"The count from the function 'count_above': {count_above(nums, limit)}")

# Q: Why is the global count still 999, even though the function set a variable called count to 0 and then increased it?
# A: The variable 'count' inside the funtion is confined there, when the function 'count_above' is called it just utputs the value 
#       of the locally defined, 'count'
