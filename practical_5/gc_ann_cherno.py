from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

GC_rec = []

for record in SeqIO.parse("dna.fasta","fasta"): #For loop that loops through each record in the dna.fasta file
    G_count=record.seq.count("G")
    C_count=record.seq.count("C")
    GC = round((100*(G_count + C_count))/len(record.seq),1)
    print(GC)
    GC_rec.append(SeqRecord((record.seq), id=record.id, description=record.id + " has GC content " + str(GC)+"%"))

SeqIO.write(GC_rec,"dna_with_gc.fasta","fasta") #Outputs all reverse-complement records to a file named dna_rc.fasta


"""
:::::::::::::::Output:::::::::::::::
(envy) chomar@GottMos:~/BIO511_python_2026_Group5/practical_5$ python gc_ann_cherno.py 
50.0
28.6
51.2
33.3
100.0
0.0
50.0
48.6
:::::::::::::::Output:::::::::::::::
"""





""" #write

SeqIO.write(dna,"out.fasta","fasta") """
