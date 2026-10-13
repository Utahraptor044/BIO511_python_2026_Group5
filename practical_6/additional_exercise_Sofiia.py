import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cnv = pd.read_csv('CNV_log2_skin_melanoma.csv')

#extracting all unique values from "chromosome" column and writing them into a list
chromosomes=[]

els = cnv["chromosome"].unique()
for el in els:
    if el not in chromosomes:
        chromosomes.append(el)

#separating autosomes and sex chromosomes into different lists to ease further sorting
autosomes = [] 
sex_chromosomes = []

for el in chromosomes:
    if el.isalpha()==True:
        sex_chromosomes.append(el)
    elif el.isdigit()==True:
        autosomes.append(int(el))

#creating the final order for xlabels on teh graph
all_chromosomes = sorted(autosomes) + sex_chromosomes

#Create a violinplot with chromosome on the x-axis and cnv_log2 on the y-axis. Add informative titles and save the plot.
sns.violinplot(data=cnv, x="chromosome", y="cnv_log2", order= all_chromosomes)
plt.title("cnv_log2 values on each chromosome")
plt.tight_layout()
plt.savefig("cnv_log2_chr_violin.jpg")


'''
sns.boxplot(data=cnv, x="chromosome", y="cnv_log2", order= all_chromosomes)
plt.title("cnv_log2 values on each chromosome")
plt.tight_layout()
plt.savefig("cnv_log2_chr_box.jpg")'''