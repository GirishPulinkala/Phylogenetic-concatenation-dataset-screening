import csv
from pprint import pprint

fasta_file = "1094.fasta"
tsv_file = "cleaner_table.tsv"

def clean_tax_file(fastaname, tsvname):
    identifiers = []
    matches=[]
    with open(fastaname, "r") as fh:
        for line in fh:
            if line.startswith(">"):
                x = line.split(":")
                identifiers.append(x[1])
                
    with open(tsvname) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            if line[0] in identifiers:
                matches.append('\t'.join(line[0:]) + '\n')
          
    return matches


fasta = clean_tax_file(fasta_file, tsv_file)
f = open("1094.tax", "a")
for line in fasta:
    f.write(line)
f.close()