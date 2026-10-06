#Extra task: GC content
sequence = "ATGCGTACTTAGCAAT"

#check if the first base is G or C
if sequence[0]=="G" or sequence[0]=="C":
    print("first base is G or C!")
else:
    print("First base is not G or C!")

#count the number of G and C bases in sequence and print it
gc_count=0
for el in range(0, len(sequence)):
    if sequence[el]=="G" or sequence[el]=="C":
         gc_count+=1
    else:
        pass
print("The number of G and C bases is:", gc_count)

#print the percentage of GC in sequence
print("GC content is:", round(gc_count/len(sequence)*100, 2), "%")

sequence2 = "TTAGGCATGCCGATATCGGCTTA"

# same for sequence2
gc_count2=0
for el in range(0, len(sequence2)):
    if sequence2[el]=="G" or sequence2[el]=="C":
         gc_count2+=1
    else:
        pass
print("The number of G and C bases is:", gc_count2)
print("GC content is:", round(gc_count2/len(sequence2)*100, 2), "%")