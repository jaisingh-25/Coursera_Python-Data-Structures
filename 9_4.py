# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:15:54 2023

@author: jaisi
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

names=[]
for i in handle:
    l=i.split()
    if i.startswith("From "):
        names.append(l[1])
        
dict={}
for j in names:
    dict[j]=dict.get(j, 0) + 1

count=0
word=""
for k in dict:
    if dict[k]>count:
        count=dict[k]
        word=k
print(word, count)