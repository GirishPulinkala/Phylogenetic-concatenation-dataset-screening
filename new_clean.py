import csv
from pprint import pprint

identifiers = []
f = open("cleaner_table.tsv", "a")
with open("clean_table.tsv", "r") as fh:
    for row in fh:
        line = row.split('\t')
        org_matrix = line[0].split('/')
        extra_name = org_matrix[3].split('.')
        if org_matrix[2] == extra_name[0]:
            new_id = org_matrix[2]+'_'+line[1]
            f.write(new_id + '\t' + line[2])
        else:
            new_id = org_matrix[2]+'_'+extra_name[0]+'_'+line[1]
            f.write(new_id + '\t' + line[2])
f.close()