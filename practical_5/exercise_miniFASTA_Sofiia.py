from Bio import Seq, SeqIO, SeqRecord

#Load and report
print("Task1. Load and report")
for seq_record in SeqIO.parse("dna.fasta", "fasta"):
    print("\nRecord ID:", seq_record.id)
    print(f"Length of {seq_record.id} is:", len(seq_record))
    print(f"First 10 bases of {seq_record.id} are:", seq_record.seq[:10])

#Reverse complements to a new FASTA
reversed_records = [seq_record.reverse_complement(id=seq_record.id + "_rc", description="reverse complement of " + seq_record.id) for seq_record in SeqIO.parse("dna.fasta", "fasta")]

SeqIO.write(reversed_records, "dna_rc.fasta", "fasta")

#GC% annotation to a new FASTA
gc_records = []

for seq_record in SeqIO.parse("dna.fasta", "fasta"):
    gc_counter = 0
    for base in seq_record.seq:
        if base == "G" or base == "C":
            gc_counter+=1
    percent_gc = round((100 * (gc_counter) / len(seq_record.seq)), 1)
    seq_record.description= "GC=" + str(percent_gc)
    gc_records.append(seq_record)

SeqIO.write(gc_records, "dna_with_gc.fasta", "fasta")

#Translation
print("\nTask4. Translation")

for seq_record in SeqIO.parse("dna.fasta", "fasta"):
    translated = seq_record.translate()
    print("\nRecord ID:", seq_record.id)
    print("First ten amino acids:", translated.seq[:10])

for seq_record in SeqIO.parse("dna_rc.fasta", "fasta"):
    print("\nRecord ID:", seq_record.id)
    print("Description:", seq_record.description)
