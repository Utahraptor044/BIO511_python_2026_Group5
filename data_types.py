#Task 1
#save one value of each data type to a variable
a = int(1)
b = float(2.0)
c = str("Hello!")
d = bool(6)
e = None
f = ["otters", "minks", "polecats"]
g = {"genus" : "Pteronura", "species" : "Pteronura brasiliensis"}
h = ("badgers", "martens", "weasels")
i = {"sables", "ermines", "grisons"}
j = range(7)

big_list = [a, b, c, d, e, f, g, h, i, j]

#print the data type of each value
for el in big_list:
    print(type(el))

#Task 2
#create an if/else-statement to determine if the string is empty or not
if len(c) != 0:
    print("non-empty")
else:
    print("empty")

#Task 3
#Write an if-statement with 3 scenarios:
#The integer could be positive
#The integer could be zero
#The integer could be negative
if a > 0:
    print("The integer is positive.")
elif a < 0:
    print("The integer is negative.")
elif a == 0:
    print("The integer is zero.")