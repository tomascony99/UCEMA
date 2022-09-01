#%%
import glob
import os
import pandas as pd

#%%
# Para listar los archivos de un directorio
os.getcwd()

#%%
path = os.getcwd() + '/04-transformaciones/'+ '/ventas_comercial/'
for file in glob.glob(path+ "/*.csv"):
    print(file)

#%%
big_frame = pd.concat([pd.read_csv(f) for f in glob.glob(path + "/*.csv")],
                      ignore_index=True)
#%%
big_frame.head()

#%%
big_frame.shape
#%%
big_frame.describe()
#%%
big_frame.info()
#%%
big_frame.isnull().sum()
#%%
big_frame.isna().sum()
#%%
big_frame.isna().sum().sum()
#%%
big_frame.isna().sum().sum() / big_frame.shape[0]
#%%
big_frame.isna().sum().sum() / big_frame.shape[0] * 100
#%%
big_frame['Play'].value_counts()
#%%
big_frame.PlayerLine.str.contains('[Kk]ing').sum()
#%%
big_frame.columns

#%%
#Aparece o no aparece la palabra Love en una columna
big_frame.PlayerLine.str.contains('[Ll]ove')
#%%
#cuantas veces aparece la palabra Love en una columna
big_frame.PlayerLine.str.count('[Ll]ove')
#%%
#crear una columna con True o False para saber si aparecio la palabra Love
big_frame['Love'] = big_frame.PlayerLine.str.contains('[Ll]ove')
#%%
#cuantas veces aparece la palabra Love en una columna
big_frame.groupby('Play').Love.value_counts()
#%%
#Quedarme solo con Love=True y ordenarlo por Play
love_df = big_frame[big_frame.Love == True]
#%%
love_df.groupby('Play').Love.value_counts()
#%%
big_frame.groupby('Play').Love.agg(['count', 'mean'])
#%%
#ordenar agrupado por obras el promedio de veces que aparecio la palabra Love
big_frame.groupby('Play').Love.agg(['count', 'mean']).sort_values('mean', ascending=False)
#%%
love_df.groupby('Play').Love.agg(['count', 'mean']).sort_values('mean', ascending=False)
#%%


#%%
with open(path + 'text.txt') as f:
    print(f.read())
#%%
text_file = open(path + "alllines.txt", "r")
#transform text file to dataframe
lines = text_file.readlines()
lines = [line.rstrip('\n') for line in lines]
lines = pd.DataFrame(lines)
lines.columns = ['lines']
lines.head()

#%%
#read a tsv file
tsv_file = pd.read_csv(path + "alllines.tsv", sep="\t")
