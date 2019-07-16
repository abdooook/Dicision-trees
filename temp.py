import numpy as np
import pandas as pd


df = pd.read_csv('diabetes.csv')
df.head()
labels=df['Outcome'].values
print(labels)