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


**run_sativa.sh**
------------
This file requires existing .mafft files as inputs, as well as a .tsv table with taxonomic information. Additionally it requires the python scripts change_fasta.py, sanity_check.py and correct_output.py. Lastly, it needs the Sativa program to be installed, and the path to this should be inserted on line 10. In addition to the Sativa standard output files this will create a .txt file listing components with possibly more than one gene, as well as .mis files with corrected taxonomic levels. To run use:
> ./run_sativa.sh

**post_process.sh**
------------
This script inputs the corrected .mis files from run_sativa.sh above, as well as the .log files from these. It also requires the summary.py script. It outputs a .txt document summarizing the number of mislabels per taxonomic level and per dataset, as well as highlight any warnings from Sativa. To run use:
> ./post_process.sh




**monophyletic_cluster-py**
------------
The program requires the input file in .treefile format
Technical Requirements: ETE3
Install ete3 using pip install ete3 in Windows command line.

Change path of ..//data//taxon.tsv to your file path

To run use:
> ./monophyletic_cluster.py -in infilepath -o outfilepath

For help run:
> ./monophyletic_cluster.py -h




