# -*- coding: utf-8 -*-
import argparse
import pandas as pd
from ete3 import Tree

parser = argparse.ArgumentParser(description='Checks for subtrees containing data from a subset of papers.')
parser.add_argument('filename', metavar='f',
                    help='Input file. Should be a newick file with the .treefile extension')
parser.add_argument('--lim_high',default = 0.95,type=float,
                    help='Minimum value for fraction of high fraction genes in a subtree')
parser.add_argument('--lim_low',default = 0.05,type=float,
                    help='Maximum value for fraction of low fraction genes in a subtree')

args = parser.parse_args()
filename = args.filename
high_lim = args.lim_high
low_lim = args.lim_low

print(high_lim)
print(low_lim)

name = filename.split("treefile")[0]

#first upload the file 14.iqtree.treefile before running
t = Tree(filename)

#take full header as input
#returns string with papername_gene
def get_gene_name(name):
  z = name.split("_")
  #if z[0] == "Chang2015":
    #return z[0] + "_" + z[-3] + "_"+ z[-2] + "_" + z[-1]
  if z[0] == "Simion2017" or z[0] == "Whelan2017" or z[0] == "Hejnol2009":
    return z[0] + "_" + z[-2] + "_" + z[-1]
  else:
    return z[0] + "_" + z[-1]

#function to check if subtree fulfills specified requirement
#checks the fraction of each paper_name. It eirher needs to be above high_lim
#or below low_lim for the subtree to pass.
def checking_children(gene_list):
  result = True
  counter = dict()
  for item in gene_list:
    if item not in counter:
      counter[item] = 0
    counter[item] += 1
  high_count = 0
  for keys in counter.keys():
    count = counter[keys]
    ref_num = dict_gene_tot[keys]
    if high_lim >= count/ref_num and count/ref_num >= low_lim:
      result = False
    if count/ref_num >= high_lim:
      high_count = high_count +1
  if high_count == len(dict_gene_tot):
    result = False
  return result

def get_fraction_list(gene_list):
  counter = dict()
  fraction_dict = {}
  for item in gene_list:
    if item not in counter:
      counter[item] = 0
    counter[item] += 1
  for keys in counter.keys():
    count = counter[keys]
    ref_num = dict_gene_tot[keys]
    fraction_dict[keys] = count/ref_num
  return fraction_dict

#cache information about node name
node_content = t.get_cached_content(store_attr='name')

#assigns paper_gene attribute to all leafs in the tree
for leaf in t.traverse():
  if leaf.is_leaf():
    leaf.add_features(gene=get_gene_name(leaf.name))

#caches information about paper_gene
node_genes = t.get_cached_content(store_attr='gene')

#makes a file with list of all paper_genes, and count the amount of each
f = open(name + "dataset_count.txt","a")
counter = {}
for node in t.traverse():
    if node.is_leaf():
      x = str(node_content[node])
      fix1 = x.replace("{", "")
      fix2 = fix1.replace("}", "")
      fix3 = fix2.replace("'", "")
      paper_name = get_gene_name(fix3)
      if paper_name not in counter:
        counter[paper_name] = 0
      counter[paper_name] += 1
text_counter = str(counter)
text_rows = text_counter.replace(":", "\t")
text_rows2 = text_rows.replace(",", "\n")
text_rows3 = text_rows2.replace("{", "")
text_rows4 = text_rows3.replace("}", "")
text_rows5 = text_rows4.replace("'", "")
text_rows6 = text_rows5.replace("\"", "")
text_rows7 = text_rows6.replace(" ", "")

splitted = text_rows7.split("\n")
splitted.sort()
strimg = "\n".join(splitted)
f.write(strimg)
f.close()

#reads in file with dataset counts to a dictionary
f = open(name + "dataset_count.txt","r")
dict_gene_tot = {}
for row in f:
  line = row.split("\t")
  dict_gene_tot[line[0]] = int(line[1])

#first round of indentifying subtrees is to be able to reroot the tree
subtree_sizes = {}
for node in t.traverse():
  if not node.is_leaf():
      if node.support > 85:
        genes = list()
        for leaf in node.traverse():
          if leaf.is_leaf():
            for item in node_genes[leaf]:
              genes.append(item)
        if len(genes) > min(dict_gene_tot.values()):  
          if checking_children(genes):
            if len(genes) not in subtree_sizes:
              subtree_sizes[len(genes)] = node
f.close

#reroot the tree based on the largest subtree
if len(subtree_sizes)==0:
  print("No subtrees fulfiling restrictions found for " + filename)
  exit()
max_subtree_size = max(subtree_sizes.keys())
largest_subtree = subtree_sizes[max_subtree_size]
t.set_outgroup(largest_subtree)

#creates a file containing a list of the contents of all subtrees with a bootstrap of 85 or higher
f = open(name + "all_subtrees.txt","a")
subtree_list = {}
for node in t.traverse():
  if not node.is_leaf():
      if node.support >= 85:
        genes = list()
        for leaf in node.traverse():
          if leaf.is_leaf():
            for item in node_genes[leaf]:
              genes.append(item)
        fraction_list = get_fraction_list(genes)
        f.write("Support: " + str(node.support) + "\t")
        f.write("Genes: ")
        for keys in fraction_list:
          item = fraction_list[keys]
          f.write(keys + ": " + str(fraction_list[keys]) + "\t")
        f.write("\n")

f.close()

#do the subtree test again
subtree_list = {}
for node in t.traverse():
  if not node.is_leaf():
      if node.support > 85:
        genes = list()
        for leaf in node.traverse():
          if leaf.is_leaf():
            for item in node_genes[leaf]:
              genes.append(item)
        if len(genes) > min(dict_gene_tot.values()):  
          if checking_children(genes):
            node.add_features(subtree_size=len(genes))
            subtree_list[node] = get_fraction_list(genes)
f.close

#Creates a dictionary only containing genes with high fraction for each subtree
subtree_high_dict = {}
for item in subtree_list:
  list_of_genes = {}
  node_dict = subtree_list[item]
  for i in node_dict:
    if node_dict[i] >= high_lim:
      list_of_genes[i] = node_dict[i]
  subtree_high_dict[item] = list_of_genes

#Compare subtrees with each other. If two subtrees contain teh exact same high fraction genes, keep the largest.
filtered_subtree_dict = {}
subtree_gene_list_dict = {}
for item in subtree_high_dict:
  item_gene_list = []
  for j in subtree_high_dict[item]:
    item_gene_list.append(j)
    item_gene_list.sort()
  subtree_gene_list_dict[item] = item_gene_list

remove_list = []
for item in subtree_high_dict:
  should_add = True
  for i in filtered_subtree_dict:
    if subtree_gene_list_dict[item] == filtered_subtree_dict[i]:
      if item.subtree_size > i.subtree_size:
        if i not in remove_list:
            remove_list.append(i)
      else:
        should_add = False
  if should_add:
    filtered_subtree_dict[item] = subtree_gene_list_dict[item]
for item in remove_list:
  filtered_subtree_dict.pop(item)

#Compare subtrees with each other. If two subtrees contain the same high fraction gene, keep the smallest.
filtered_subtree_dict_2 = {}
remove_list = []

for item in filtered_subtree_dict:
  to_add = True
  for i in filtered_subtree_dict_2:
    to_remove = False
    for element in subtree_gene_list_dict[item]: 
      if element in filtered_subtree_dict[i]:
        if len(filtered_subtree_dict[i]) > len(subtree_gene_list_dict[item]):
          if i not in remove_list:
            remove_list.append(i)
        else:
          to_add = False
  if to_add:
    filtered_subtree_dict_2[item] = filtered_subtree_dict[item]
for item in remove_list:
  filtered_subtree_dict_2.pop(item)

to_remove = []
for item in filtered_subtree_dict_2:
  if len(filtered_subtree_dict_2[item]) == 0:
    to_remove.append(item)
for item in to_remove:
  filtered_subtree_dict_2.pop(item)

#Print list of the best subtrees to a file.
#Print newick trees of the best subtrees to a file.
f = open(name + "best_clusters_filtered.txt","a")
g = open(name + "best_trees.nw","a")
tree_count =len(filtered_subtree_dict_2)
final_tree_bootstrap_fraction = {}
for keys in filtered_subtree_dict_2:
  g.write(keys.write())
  tree_count = tree_count-1
  if tree_count != 0:
    g.write("\n\n")
  item = subtree_list[keys]
  f.write(str(keys.support) + "\t")
  for i in item:
    f.write(i + ": " + str(item[i]) + "\t")
  f.write("\n")

f.close()