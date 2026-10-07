my_int = 4
print(my_int)
print(type(my_int))

floater = 4.5
print(floater)
print(type(floater))

statement = "South park rules"
print(statement)
print(type(statement))

boolean = 5>3
print(boolean)
print(type(boolean))

derp = None
print(derp)
print(type(derp))

listing = ["dylan","dylan","andDylan"]
print(listing)
print(type(listing))

dict = {"name": "Cherno", "midname": "Omar"}
print(dict)
print(dict.values())
print(type(dict))

tupp = ("julafton","juldagen","")
print(tupp)
print(type(tupp))

onMyset = {"set1","set2","set3","set1","set1","set3"}
print(onMyset)
print(type(onMyset))

ranger = range(15)
print(ranger)
print(type(ranger))

if "dylan" in listing:
    print("yup, Dylan is here")

    print(listing[2])

length = len(statement)

if length != 0:
    print("non-empty")
elif length == 0:
    print("emtpy")

if my_int >= 0:
    print("positive integer")
elif my_int == 0:
    print("zero integer")
elif my_int <= 0:
    print("negative integer")  

if tupp is list or tuple or range:
    if len(tupp) == 0:
        print("empty")
    elif len(tupp) == 1:
        print("tuple is not empty")
    elif len(tupp) >= 1:
        print("multiple items")

read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}
print("sample_A" in read_counts)

sample = "sample_A"
passed_qc = False

if sample not in read_counts:
    print("unknown sample")
elif read_counts[sample] is None:
    print("sequencing failed")
elif read_counts[sample] > 1000000 and passed_qc:
    print("ready for analysis")
else:
    print("too few reads")