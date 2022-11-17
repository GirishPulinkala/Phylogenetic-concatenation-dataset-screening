import csv
from pprint import pprint

identifiers = []
f = open("cleaner_table.tsv", "a")
with open("clean_table.tsv", "r") as fh:
    for row in fh:
        line = row.split('\t+')
        if line[0] not in identifiers:
            identifiers.append(line[0])
            f.write('\t'.join(line[0:]))
            
f.close()