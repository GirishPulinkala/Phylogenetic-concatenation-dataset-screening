import sys
import csv
from collections import Counter

mislabel_taxa = open(sys.argv[1], "r")    #arg[1] = corrected output .mis file
f = open(sys.argv[2], "a")    #arg[2] = name of summary file
log_file = open(sys.argv[3], "r") #arg[3] = log file for sativa run


tsv_file = csv.reader(mislabel_taxa, delimiter="\t")
levels = []
papers = []
f.write("\n"+"----------"+"\n"+"Summary of "+sys.argv[1]+"\n")
for line in tsv_file: #Check for the level of mislabels, check for which dataset & summarize in dictionary
    level = line[1] 
    levels.append(level)
    header = line[0].split("_")
    paper_name = header[0]
    papers.append(paper_name)
f.write("Putative mislabels on different levels:"+"\n")
f.write(str(dict(Counter(levels)))+"\n")
f.write("Putative mislabels per dataset:"+"\n")
f.write(str(dict(Counter(papers))))

for line in log_file:
    if line.startswith("WARNING: F"):
        continue
    elif line.startswith("WARNING:"):
        f.write("\n"+"Other warnings from SATIVA:")
        f.write("\n"+line+" See "+sys.argv[3]+" for more information")




