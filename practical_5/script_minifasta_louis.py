print("It works !")

from Bio.Seq import Seq
from Bio import SeqIO

for seq_record in  SeqIO.parse("dna.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq[0:10]))
    reversed_seq = seq_record.seq.reverse_complement()
    print(reversed_seq)
    print(len(seq_record))

#return the sequence

#create an empty list, and add the reverse sequence


