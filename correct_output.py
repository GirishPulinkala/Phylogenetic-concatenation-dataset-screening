from ete3 import NCBITaxa
import sys
import csv
from pprint import pprint

ncbi = NCBITaxa()
mislabel_taxa = open(sys.argv[1], "r")    #arg[1] = sativa output .mis file
f = open(sys.argv[2], "a")    #arg[2] = name of corrected output file
tsv_file = csv.reader(mislabel_taxa, delimiter="\t")
next(tsv_file, None) 
next(tsv_file, None)
next(tsv_file, None) 
next(tsv_file, None) 
next(tsv_file, None) 
for line in tsv_file:
    name = str(line[2])  
    name2taxid = ncbi.get_name_translator([name])  #get taxid from label
    classes = name2taxid[name]  #get the taxid
    level = ncbi.get_rank(classes)  #get rank of label
    level_name = level[int(classes[0])]  #get only the rank name
    f.write(line[0]+"\t"+level_name+"\t"+line[2]+"\t"+line[3]+"\t"+line[4]+"\n")
