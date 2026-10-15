print("It works !")

import sys
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


input = sys.argv[1:]
file = input[0]
print(type(file))

for seq_record in  SeqIO.parse(file, "fasta"):
    print(seq_record.id)
    # repr make print the data as they are stored
    print(repr(seq_record.seq[0:10]))
    # recreate the complementary sequence and reverse it
    reversed_seq = seq_record.seq.reverse_complement()
    print(reversed_seq)
    print(len(seq_record))

#return the sequence

#create an empty list, and add the reverse sequence

with open (file, "r") as input, open ("reversed_dna.fasta", "w") as output:

    for seq_record in SeqIO.parse(input, "fasta"):
        print(seq_record.id)
        # Create the inverse sequence but only the sequence
        reverse_seq = seq_record.seq.reverse_complement()
        #Assemble toutes les infos nécessaires.
        reverse_record = SeqRecord(
            reverse_seq,
            id=seq_record.id + "_rc",
            description="Reverse complement of " + seq_record.id
        )

        print(reverse_seq)
        SeqIO.write(reverse_record, output, "fasta")


