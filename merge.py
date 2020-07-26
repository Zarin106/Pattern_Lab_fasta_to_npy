# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 08:17:50 2020

@author: User
"""

import pandas as pd
from numpy import save
data = pd.read_csv("output4_split_4000_kmer3.txt", header = None)
data1 = pd.read_csv("output4_split_8000_kmer3.txt", header = None)
data2 = pd.read_csv("output4_split_12000_kmer3.txt", header = None)

data.append(data1)
data.append(data2)

del data[0]
print(data)
save('A.thaliana5289_pos_kmer3.npy', data)
