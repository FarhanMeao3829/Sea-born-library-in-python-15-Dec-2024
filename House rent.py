import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("USA_Housing.csv")
print(df.head(10))

print(df.info())

print(df.describe)

print(df.columns)

# sns.pairplot(df)

df = df.drop(columns = ['Address'])

sns.heatmap(df.corr(), annot= True)
plt.show()