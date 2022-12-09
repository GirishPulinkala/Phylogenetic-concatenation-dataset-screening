import csv
from pprint import pprint
import sys

# command line called by python3 change_fasta.py number.mafft number_renamed.fasta number.tax cleaner_table2.tsv

#input alignment file:
fasta_file = sys.argv[1]
# output alignment_renamed.fasta file:
renamed_fasta = sys.argv[2]
#sys.argv3 = number.tax
f = open(sys.argv[3], "a")
# input tsv taxon table:
tsv_file = sys.argv[4]

def change_fasta(fastaname, outfastaname):
    identifiers = []
    f = open(outfastaname, "a")
    with open(fastaname, "r") as fh:
        for line in fh:
            if line.startswith(">"):
                x = line.split(":")
                f.write(x[0]+"_"+x[1]+"\n")
            else:
                f.write(line)
    f.close()
                

def clean_tax_file(fastaname, tsvname):
    identifiers = []
    matches=[]
    with open(fastaname, "r") as fh:
        for line in fh:
            if line.startswith(">"):
                identifiers.append(line[1:-1])   
    with open(tsvname, "r") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            if line[0] in identifiers:
                matches.append('\t'.join(line[0:]) + '\n')
          
    return matches

fasta = change_fasta(fasta_file, renamed_fasta)
matches_list = clean_tax_file(renamed_fasta, tsv_file)
for line in matches_list:
    f.write(line)
f.close()