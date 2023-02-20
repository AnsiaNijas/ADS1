# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:44:52 2023

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
all_words=[]
counter=0
for line in text:
    words=line.split()
    counter += 1
    for word in words:
        word=cl.clean(word)
        all_words.append(word)
print(all_words)
df_words=pd.DataFrame(data=all_words, columns=('words',))
df_words=df_words.value_counts()
print(df_words)
df_words.to_csv('words_count.csv')

print(len(all_words))

nchar=0
for word in all_words:
     nchar = nchar + len(word)  
print(nchar)

