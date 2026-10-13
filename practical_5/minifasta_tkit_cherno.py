from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

revc = []

for record in SeqIO.parse("dna.fasta","fasta"): #For loop that loops through each record in the dna.fasta file
        print(record.id,len(record.seq))        #Prints the record ID and the sequence length 
        print(record.seq[0:10])                 #Prints only the first 10 bases of the sequene
        revc.append(record.reverse_complement(id=record.id + "_rc",description="reverse complement of " + record.id)) #For each record, creates new SeqRecord and appends it to the revc list
                                                                                                                    
SeqIO.write(revc,"dna_rc.fasta","fasta") #Outputs all reverse-complement records to a file named dna_rc.fasta

"""
:::::::::::::::Output:::::::::::::::
(envy) chomar@GottMos:~/BIO511_python_2026_Group5/practical_5$ python fasta_tkit_cherno.py 
seq1 28
ATGCATGCAT
seq2 21
GATTACAGAT
seq3 41
CGCGATATCG
seq4 18
TTTAAACCCG
seq5 30
GCCGCGGCGC
seq6 22
ATATATATAT
seq7 32
ACGTTGCAAC
seq8 37
CATGACTGAC:::::::::::::::Output:::::::::::::::
"""