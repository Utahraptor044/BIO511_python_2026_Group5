#Task 1
#save one value of each data type to a variable
a = int(1)
b = float(2.0)
c = str("Hello!")
d = b<a
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
