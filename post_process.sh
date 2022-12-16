#!/bin/bash
for f in corrected_*.mis
do
  echo "$f"
  suffix="${f##*[0-9]}"
  number="${f%"$suffix"}"
  number="${number##*[!-0-9]}"
  python3 summary.py corrected_${number}.mis summary.txt test_${number}.log
done