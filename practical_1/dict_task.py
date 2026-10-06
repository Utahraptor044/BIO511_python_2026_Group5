#Task 5
read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}
sample = "sample_A"
passed_qc=True
if sample in read_counts:
    if read_counts[sample] is None:
        print("sequencing failed")
    elif read_counts[sample]>1000000 and passed_qc:
        print("ready for analysis")
    else:
        print("too few reads")
else:
    print("unknown sample")