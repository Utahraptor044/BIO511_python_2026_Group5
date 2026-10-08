sequence = "ATGCGTACTTAGCAAT"

# Are the first nucleotides a G or C?
if sequence[0] == "G" or sequence[0] == "C":
    print("The first nucleotide is a G or C")
else:
    print("The first nucleotide is a T or A")

gc_count = 0
for nucleotide in sequence:
    if nucleotide == "G" or nucleotide == "C":
        gc_count+=1

print("There are ", gc_count, " G or C nucleotides in the sequence")
print("the GC content is ", gc_count/len(sequence)*100, "%")
