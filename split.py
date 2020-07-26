# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 05:48:32 2020

@author: User
"""

lines_per_file = 4000
smallfile = None
with open('output4.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'output4_split_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()