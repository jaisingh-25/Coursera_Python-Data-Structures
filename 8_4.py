# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:48:42 2023

@author: jaisi
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    a=line.split()
    for i in a:
        if i not in lst:
            lst.append(i)
print(sorted(lst))
