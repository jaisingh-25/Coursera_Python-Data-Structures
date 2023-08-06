# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:31:12 2023

@author: jaisi
"""

text = "X-DSPAM-Confidence:    0.8475"
a=text.find("0")
print(float(text[a:]))
