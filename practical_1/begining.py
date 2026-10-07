#Data types to include: integer, floating point, string, boolean, 
#nonetype, list, dictionary, tuple, set, range.

myint = 10
#print(type(myint), ": ", myint)
#if myint < 0:
#    print("Integer is negative")
#elif myint == 0:
#    print("Integer is zero")
#else:
#    print("Integer is positive")

myfloat = 3.14
#print(type(myfloat), ": ", myfloat)

mystring = "Hello, World!"
#print(type(mystring), ": ", mystring)
#if len(mystring) == 0:
#    print("String is empty")
#elif len(mystring) < 0:
#    print("wtf bro")
#else:
#    print("String is not empty")

mybool = False
#print(type(mybool), ": ", mybool)

mynone = None
#print(type(mynone), ": ", mynone)

mylist = [1, 2, 3, 4, 5]
#print(type(mylist), ": ", mylist)

mydict = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}
print(type(mydict), ": ", mydict)
print("sample_A" in mydict)

sample = input("Enter sample name: ")
passed_qc = False
print(sample)
if sample in mydict:
    if mydict[sample] is None:
        print("Sequencing failed")
    elif mydict[sample] > 1000000:
        if passed_qc ==True:
            print("Ready for analysis")
        else:
            print("Enough reads")
    else :
        print("Not enough reads")
else:
    print("Sample not found in dictionary. Type sample_ and a capital letter")



mytuple = (1, 2, 3)
#print(type(mytuple), ": ", mytuple)

myset = {1, 2, 3, 4, 5}
#print(type(myset), ": ", myset)

myrange = range(5)
#print(type(myrange), ": ", myrange)

mysequence = mytuple
#if type(mysequence) == range or type(mysequence) == list or type(mysequence) == tuple:
#    print(len(mysequence))
#    if len(mysequence) > 1:
#         print("Multiple items")
#    elif len(mysequence) == 1:
#        print("Single item")
#     else:
#         print("No items")
# else:
#     print("Wrong type for this task. Please choose a range, list or tuple")
    

