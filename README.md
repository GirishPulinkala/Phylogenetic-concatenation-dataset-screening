# Phylogenetic-concatenation-dataset-screening
Building an automated workflow to identify putative mislabels in taxonomies, using python packages


**filter_subtrees_dataset.py**
Is run with an input .treefile. Has two optional paramterers fraction high lim and fraction low lim which are set to 0.95 and 0.05 respectively by default. To run use:
> python3 filtered_list.py treefile

with default values.

> python3 filtered_list.py treefile --lim_high 0.95 --lim_low 0.05

with specific values.
