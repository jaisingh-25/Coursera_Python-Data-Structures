# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:48:47 2023

@author: jaisi
"""

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for i in fh:
    if i.startswith("From "):
        a=i.split()
        print(a[1])
        count+=1

print("There were", count, "lines in the file with From as the first word")
