# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:27:44 2023

@author: an22adx
"""

import clean_up as cl
import pandas as pd

help(cl.clean)
print(cl.clean("ANSIA1232"))

text=open("big_data.txt")
print(text)
text_df=pd.read_csv("big_data.txt", sep="/s")
print(text_df)
all_letters=[]
counter=0

for line in text:
    words=line.split()
    counter += 1
  
    for word in words:
        word=cl.clean(word)
        letters=list(word)
        for l in letters:
            all_letters.append(l)
print(all_letters)
df_char=pd.DataFrame(data=all_letters, columns=('letters',))
df_char=df_char.value_counts()
print(df_char)
df_char.to_csv('character_count.csv')