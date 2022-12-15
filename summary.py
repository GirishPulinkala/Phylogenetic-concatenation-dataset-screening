import sys
import csv
from collections import Counter

mislabel_taxa = open(sys.argv[1], "r")    #arg[1] = corrected output .mis file
f = open(sys.argv[2], "a")    #arg[2] = name of summary file
tsv_file = csv.reader(mislabel_taxa, delimiter="\t")
levels = []
papers = []
for line in tsv_file:
    level = line[1] 
    levels.append(level)
    header = line[0].split("_")
    paper_name = header[0]
    papers.append(paper_name)
f.write("summary of "+sys.argv[1]+"\n")
f.write(str(dict(Counter(levels)))+"\n")
f.write(str(dict(Counter(papers))))

