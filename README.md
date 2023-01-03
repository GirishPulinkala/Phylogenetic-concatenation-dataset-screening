# Phylogenetic-concatenation-dataset-screening
Building an automated workflow to identify putative mislabels in taxonomies, using python packages




**filter_subtrees_dataset.py**
------------

Is run with an input .treefile. Has two optional paramterers fraction high lim and fraction low lim which are set to 0.95 and 0.05 respectively by default. It outputs several files. One dataset_count.txt that counts the amount of different paper_gene leaves, all_subtrees.txt which contain the fraction of all paper_gene in every possible subtree with a bootstrap of 85 or higher, best_clusters_filtered.txt which contain the same infor as all_subtrees.txt but only for the best subtrees determined by the script, lastly best_trees.nw is a files containing the newick format trees for all the best subtrees.  To run use:
> python3 filter_subtrees_dataset.py treefile

with default values.

> python3 filter_subtrees_dataset.py treefile --lim_high 0.95 --lim_low 0.05

with specific values.

OBS! Make sure the first method get_gene_name(name) is updated according to the input data before running.

ETE3, argparse, and pandas has to be installed to run.
