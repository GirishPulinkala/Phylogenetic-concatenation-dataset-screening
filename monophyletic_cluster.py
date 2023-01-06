#!/usr/bin/env python
# coding: utf-8




import pandas as pd
from ete3 import Tree
import numpy as np
import csv
import sys




def change_names(name):
    new_name=name.split('_')
    




def check_taxid(c): #Data processing step to check tax_id from dataset 
    for i in reversed(c[:-1]):
        if i.isdigit():
            if len(i)>3:
                return(i)





def check_phyla(f):#Data processing step to check phylum from dataset
    if f in tax_id.keys():
        return(tax_id.get(f))





def add(dic, key, value): #Data processing step to map phylum to each taxa in tree
        value=value
        if key in dic.keys():
            dic[key].append(value)
        else:
            dic[key]= []
            dic[key].append(value)
        return dic





def check_phylanames(val,f): #Concluding step to map phylum to taxa identified as a mislabel
    k=[]
    
    for i in val:
        for key,values in dic.items():
            if i in values:
                if key==f:
                    k.append([i, key])
    return k
    





def get_key(val): #Processing step to map a monophyletic clusters as a specific phylum 
    for key,values in dic.items():
        if val in values:
            return key





def get_mislabel(treee): #Processing step to identify mislabels in clusters
    co={j:treee.count(j) for j in treee}
    #fu={j:tree for j in treee}
    return co





def get_index(data):
    for i in data:
        if sum(i.values())>16 and sum(i.values())<maximum and len(i)>1:
            print(data.index(i))





def get_prop(ff): #Concluding step to get proportions of potential mislabel in the cluster 
    s = sum(ff.values())
    for k, v in ff.items():
        pct = v * 100.0 / s

    if pct<20:
        return k





def output_results(outfile,mislabel):#Writes the output into .txt file
    with open(outfile,'w') as f:
        wr = csv.writer(f)
        wr.writerows(mislabels)




argumentList = sys.argv[1:]
options = "hio:"
long_options = ["Help", "input=", "output="]
 
try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("monophyletic_cluster.py -in filepath -o outfilepath ")
             
        elif currentArgument in ("-in", "--input"):
            infile=sys.argv[1]
             
        elif currentArgument in ("-o", "--output"):
            outfile=sys.argv[2]
             
except getopt.error as err:
    print (str(err))
    
t = Tree(infile,format=0) #Read tree file

df=pd.read_csv("..//taxon_table.tsv", sep='\t') 

tax_id=dict(zip(df.ncbi_tax_id,df.clade_assignment))

mapped_taxa={} #contains leaf nodes in the tree mapped to a particular phylum
count=0
for leaf in t:
    name=leaf.name
    leaf_name=name.split('_')
    tax_ids=int(check_taxid(leaf_name))
    phyla_name=check_phyla(tax_ids)
    mapped_taxa=add(mapped_taxa,phyla_name,leaf.name)
    


node_content = t.get_cached_content(store_attr='name')

subtree=[]
for node in t.traverse():
    if not node.is_leaf():
        taxa=list(node_content[node])
        subtree.append(taxa)


phylum=[]
cluster_count=[] #contains number of taxa belonging to a phylum in a cluster
for i in subtree:
    sub=[]
    for j in i:
        sub.append(get_key(j))
    phylum.append(sub)

for i in phylum:
    cluster_count.append(get_mislabel(i))


uni=np.array([])
for i in subtree:
    uni=np.append(uni,len(i))
unique=(np.unique(uni)) #contains distinct sizes of monophyletic clusters

maximum=np.percentile(unique,75)


check_clusters=[] #contains tree sizes which can be checked for mislabels
for i in cluster_count:
        if sum(i.values())>16 and sum(i.values())<maximum and len(i)>1:
            check_clusters.append(data.index(i))


mislabels=[] #llist of problematic taxa with their phylum
for i in check_clusters:
    t=(check_phylanames(l[i],get_prop(data[i])))
    if t not in mislabels:
        mislabels.append(t)







