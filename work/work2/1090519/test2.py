import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
print(df['a'].describe()['std'])
print(df['a'].std(ddof=0))
