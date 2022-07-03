
import pandas as pd

f=open(r'apa.txt')
pos=f.read()

dataframe=pd.read_csv("apa.txt",delimiter="####")


dataframe.to_csv("output.csv",index=None)
print(pos)



