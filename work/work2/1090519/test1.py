import pandas as pd

df = \
    pd.read_csv(r'..\voteData\2010村里長\elcand.csv',
                names=['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'name', 'c7', 'gender', 'birthYear', 'c10', 'c11', 'c12',
                       'c13', 'elected', 'c15'])

df['age'] = 99 - df.birthYear
# print(df.age.describe())
# print(df.age.describe()['mean'])
# print(df.age.describe()['std'])


df = df.sample(30)
mu = df['age'].describe()['mean']
std = df['age'].std()
print(mu - 1.96 * std, mu + 1.96 * std)
