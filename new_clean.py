import csv
from pprint import pprint

identifiers = []
f = open("cleaner_table.tsv", "a")
with open("clean_table.tsv", "r") as fh:
    for row in fh:
        line = row.split('\t')
        org_matrix = line[0].split('/')
        new_id = org_matrix[2]+'_'+line[1]
        f.write(new_id + '\t' + line[2])
            
f.close()