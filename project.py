import numpy as np
import pandas as pd
r=pd.read_csv('abc.csv')
print(r.head())
print(r.describe())
print(r.shape)
print(r.all())
print(r.columns)
print(r.duplicated())
print(r.dtypes)
print(r.nunique())
print(r.value_counts())

print(np.mean)
ls=r[(r["Region"]=="South") & (r["Category"]=="Technology")]
print(ls)
