# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 04:43:11 2020

@author: User
"""

from Bio import SeqIO

fasta_sequences = SeqIO.parse(open("A.thaliana5289_pos.fasta"),'fasta')
with open("output4.txt", "a") as myfile: #output.txt file should be opened first
  i=0
  for fasta in fasta_sequences:
      name, sequence = fasta.id, str(fasta.seq)
      print(name, sequence)
      myfile.write(">"+ str(i) + '|1|training\n'  + sequence + '\n')
      i+=1
