#!/bin/bash
for f in *.mafft
do
  base=${f%.mafft}
  echo ${base}
  python3 change_fasta.py ${base}.mafft ${base}_renamed.fasta ${base}.tax dosReis_table.tsv
  outputString=`python3 sanity_check.py ${base}_renamed.fasta`
  if test -z "$outputString" 
  then 
    python3 /home/andraalma/sativa.py -s ${base}_renamed.fasta -t ${base}.tax -x ZOO -T 2 -n test_${base} 
    python3 correct_output.py test_${base}.mis corrected_${base}.mis
  else 
    echo "Multiple genes! Will not run SATIVA on component ${base}"
  fi
  

done
