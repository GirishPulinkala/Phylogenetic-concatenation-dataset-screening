#!/usr/bin/env python
# coding: utf-8

import sys

infile= sys.argv[1]
infile_2=sys.argv[2]



with open (infile, "r") as f:
    data=f.readlines()


p_number = re.compile('([A-Za-z0-9]+(_[A-Za-z0-9]+)+)')


ete_list=[]
for s in data:
        match = p_number.findall(s)
        if match:
            ete_list.append(match)

ete_set=set()
for i in (ete_list):
        for j in i:
            if len(j[0])>10:
                ete_set.add(j[0])

j=[]
for i in g:
    t=i.split('_')
    j.append(('_'.join(t[:3])))


with open (infile_2, "r") as f:
    data=f.readlines()


hum=re.compile('([A-Za-z0-9]+(_[A-Za-z0-9]+)+)')


hi=[]
for i in data:
    match = hum.findall(i)
    if match:
            hi.append(match)


o=set()
for i in (hi):
        for j in i:
            if len(j[0])>10:
                o.add(j[0])


print(set(j)&o)


