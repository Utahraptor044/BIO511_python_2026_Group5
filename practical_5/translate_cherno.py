from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


for record in SeqIO.parse("dna.fasta","fasta"): #For loop that loops through each record in the dna.fasta file
        trans = record.seq.translate()     
        print(trans)  
        print(trans[0:10])
        
for record_rc in SeqIO.parse("dna_rc.fasta","fasta"): #For loop that loops through each record in the dna.fasta file
        
        print(record_rc)                                                                                                                    

"""
:::::::::::::::Output:::::::::::::::
(envy) chomar@GottMos:~/BIO511_python_2026_Group5/practical_5$ python translate_cherno.py 
/home/chomar/miniconda3/envs/envy/lib/python3.15/site-packages/Bio/Seq.py:2874: BiopythonWarning: Partial codon, len(sequence) not a multiple of three. Explicitly trim the sequence or add trailing N before translation. This may become an error in future.
  warnings.warn(
MHACMHACM
MHACMHACM
DYRLQIT
DYRLQIT
RDIAISRYRDIAI
RDIAISRYRD
FKPGFK
FKPGFK
AAARRGAPRR
AAARRGAPRR
IYIYIYI
IYIYIYI
TLQRCNVATL
TLQRCNVATL
HD*LMLAS*SYD
HD*LMLAS*S
ID: seq1_rc
Name: seq1_rc
Description: seq1_rc reverse complement of seq1
Number of features: 0
Seq('GCATGCATGCATGCATGCATGCATGCAT')
ID: seq2_rc
Name: seq2_rc
Description: seq2_rc reverse complement of seq2
Number of features: 0
Seq('TGTAATCTGTAATCTGTAATC')
ID: seq3_rc
Name: seq3_rc
Description: seq3_rc reverse complement of seq3
Number of features: 0
Seq('GATATCGCGATATCGCGATATCGCGATATCGCGATATCGCG')
ID: seq4_rc
Name: seq4_rc
Description: seq4_rc reverse complement of seq4
Number of features: 0
Seq('TTTAAACCCGGGTTTAAA')
ID: seq5_rc
Name: seq5_rc
Description: seq5_rc reverse complement of seq5
Number of features: 0
Seq('GCGCCGCGGCGCGCCGCGGCGCGCCGCGGC')
ID: seq6_rc
Name: seq6_rc
Description: seq6_rc reverse complement of seq6
Number of features: 0
Seq('ATATATATATATATATATATAT')
ID: seq7_rc
Name: seq7_rc
Description: seq7_rc reverse complement of seq7
Number of features: 0
Seq('TGCAACGTTGCAACGTTGCAACGTTGCAACGT')
ID: seq8_rc
Name: seq8_rc
Description: seq8_rc reverse complement of seq8
Number of features: 0
Seq('GATCGTACGATCAGCTAGCTAGCATCAGTCAGTCATG')
CATGACTGAC:::::::::::::::Output:::::::::::::::
"""
