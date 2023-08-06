# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:01:34 2023

@author: jaisi
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict={}
for i in handle:
    l=i.split()
    if i.startswith("From "):
        hr=l[5][:2]
        dict[hr]=dict.get(hr, 0) + 1

for k,v in sorted(dict.items()):
    print(k,v)

# #List Comprehension short code
# print(sorted([(k,v) for k,v in dict.items()]))