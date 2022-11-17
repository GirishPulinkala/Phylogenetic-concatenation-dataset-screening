import csv
from pprint import pprint

fasta_file = "1094.fasta"
out_fasta = "1094_renamed.fasta"

def change_fasta(fastaname, outfastaname):
    identifiers = []
    f = open(outfastaname, "a")
    with open(fastaname, "r") as fh:
        for line in fh:
            if line.startswith(">"):
                x = line.split(":")
                f.write(">"+x[1]+"\n")
            else:
                f.write(line)
    f.close()
                
                


fasta = change_fasta(fasta_file, out_fasta)