#!/usr/bin/env python
# coding: utf-8

# In[235]:


import pandas as pd
from ete3 import Tree


# In[19]:


get_ipython().system('pip install ete3')


# In[236]:


t = Tree("C://Users//giris//Downloads//11.iqtree.treefile",format=0)


# In[383]:


for node in t:
    print(node)


# In[64]:


print(t)


# In[65]:


df=pd.read_csv("C://Users//giris//Downloads//taxon_table.tsv", sep='\t')


# In[62]:


df


# In[66]:


tax_id=dict(zip(df.ncbi_tax_id,df.clade_assignment))
tax_id


# In[41]:


if 'Apis_mellifera' in df['relabelled_name'].values:
    print('true')


# In[67]:


def change_names(name):
    new_name=name.split('_')
    


# In[68]:


name=df['relabelled_name'][1]
n,s=name.split('_')


# In[69]:


f = pd.DataFrame(columns=['A','B'])
f


# In[70]:


l=[]
dic={}
count=0
for leaf in t:
    name=leaf.name
    c=name.split('_')
    #print(c)
    #print('*********')
    v=int(check_taxid(c))
    #print(v)
    g=check_phyla(v)
    #print(g)
    dic=add(dic,g,leaf.name)
    print(dic)
    #print(v)
#print(count)


# In[78]:


print(dic['Porifera'])


# In[72]:


def check_taxid(c):
    for i in reversed(c[:-1]):
        if i.isdigit():
            if len(i)>3:
                return(i)


# In[73]:


def check_phyla(f):
    if f in tax_id.keys():
        return(tax_id.get(f))


# In[74]:


def add(dic, key, value):
        value=[value]
        if key in dic.keys():
            dic[key].append(value)
        else:
            dic[key]= []
            dic[key].append(value)
        return dic


# In[75]:


d={}
d["kk"] = [20]
if 'kk' in d:
    d['kk'].append('gg')
    print(d)
else:
    d['kk']=v


# In[76]:


d['kk']='jj'
print(d)


# In[77]:


Details = {}
Details["Age"] = [20]
print(Details)
  
if "Age" in Details:
    Details["Age"].append("Twenty")
    print(Details)


# In[274]:


s=dic['Porifera']
print(len(s))


# In[ ]:


print (t.check_monophyly(values=s, target_attr="name"))


# In[180]:


for i in dic.keys():
    print(i)


# In[390]:


print(dic['Fungi'])


# In[388]:


node=t.search_nodes(name='dosReisDonoghueYang_2015_superalignment_Amphimedon_queenslandica_400682_vacaatpasepl21-a')[0]


# In[387]:


#flag=7
val=True
while val is True:
    print(check_node(node))
   # print(node)
    for leaf in node:
        if leaf.name in s:
            #print(node)
            continue
        else:
            #print(leaf.name)
            val=False
            break
    #print(node)
    node=node.up


#print(node.support)


# In[307]:


print(dic[None])


# In[371]:


flag=7
val=True
while val is True:
   # print(node)
    for leaf in node:
        if leaf.name in s:
            continue
        else:
            break
    print(node)
    node=node.up


print(node.support)


# In[389]:


flag=7
val=True
while val is True:
    #print(node)
    for leaf in node:
        if leaf.name in s:
            continue
        else:
            break
    print(node)
    print(node.support)
    node=node.up


# In[139]:


t=t-t.prune(s)
print(t)


# In[195]:


new_tree=Tree()


# In[205]:


new_tree.add_child(node)


# In[206]:


print(new_tree)


# In[ ]:


flag=7
val=True
while val is True:
   # print(node)
    for leaf in node:
        if leaf.name in s:
            continue
        else:
            break
    print(node)
    node=node.up


print(node.support)


# In[302]:


def check_node(node):
    for leaf in node:
        if leaf.name not in tax_list:
            return(leaf.name)


# In[253]:


if ('Hejnol2009_Trichinella_spiralis_6334_Tribe1506_0') in dic['Porifera']:
    print(True)
else:
    print(False)


# In[396]:


for node in t.traverse("preorder"):
    if node.name == '':
        node.name = 'Internal node'
    print (node.name)


# In[398]:


node_content = t.get_cached_content(store_attr='name')


# In[405]:


print(node_content)


# In[419]:


l=[]
for node in t.traverse():
    if not node.is_leaf():
        f=list(node_content[node])
        print(f)
        print('********')
        for i in f:
            if i not in s:
                l.append(i)
                
        #print(type(node_content[node]))
print(l)


# In[ ]:


def check_phylanames(l):
    
    

