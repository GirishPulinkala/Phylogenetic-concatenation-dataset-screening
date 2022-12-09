#!/bin/bash
for f in *.mafft
do
  base=${f%.mafft}
  echo ${base}
  python3 change_fasta.py ${base}.mafft ${base}_renamed.fasta ${base}.tax cleaner_table2.tsv
done
