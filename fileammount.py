#find the number of files in a dir
import os.path
import pathlib
import read
import write
import pandas as pd

w = write
r = read
lib = pathlib.Path
p = lib(__file__).parents[1]

SDRIVE = lib('C:/Users/croberts/Desktop/compare/SDRIVE')
COMPARISON_FILE = lib(str(p) + '/out/count.csv')

def get_comparison(fname):
    fname = r.read_csv(fname)
    fname = fname.values.tolist()
    return pd.DataFrame(fname).dropna()

def count(path):
    return sum(len(files) for _, _, files in os.walk(path))

df = get_comparison(COMPARISON_FILE)

temp = []

for i in range(len(df)):
    # print([df.iloc[i,2], count(df.iloc[i,0]), df.iloc[i,2], count(lib(df.iloc[i,1]))])
    # temp.append([lib(df.iloc[i,2]), count(lib(df.iloc[i,0])), lib(df.iloc[i,2]), count(lib(df.iloc[i,1]))])
    temp.append([lib(df.iloc[i,1]), count(lib(df.iloc[i,0]))])


w.write_csv(lib(f'{p}/cool'), pd.DataFrame(temp))