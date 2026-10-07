sequence = "ATGCGTACTTAGCAAT"

#1 Check one base.

if sequence[0] == "G" or sequence[0] == "C":
    print("first base is a G or C")
else:
    print("the first base is not a G or a C")

#2 Count the G and C bases.

gc_count = 0

for base in sequence:
    if base == "G" or base == "C":
        gc_count += 1
        
print(f"Total number of G or C bases is {gc_count}")

#3 Calculate the GC content.

GC_content = gc_count/len(sequence)*100

print(f"GC content in the first sequence is {GC_content}%")

#4 A new sequence arrives.

sequence2 = "TTAGGCATGCCGATATCGGCTTA"

gc_count2 = 0

for base in sequence2:
    if base == "G" or base == "C":
        gc_count2 += 1

GC_content2 = round((gc_count2/len(sequence2)*100),2) #Rounded to 2 decimals

print(f"GC content in the second sequence is {GC_content2}%")
