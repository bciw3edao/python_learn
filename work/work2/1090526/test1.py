import pandas as pd

df = \
    pd.read_csv(r'..\voteData\2010村里長\elcand.csv',
                names=['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'name', 'c7', 'gender', 'birthYear', 'c10', 'c11', 'c12',
                       'c13', 'elected', 'c15'])

df['age'] = 99 - df.birthYear

import sqlalchemy

engine = \
    sqlalchemy.create_engine("mssql+pyodbc://sa:@1qaz2wsx@192.168.1.86,1433/"
                             "test?driver=SQL+Server+Native+Client+11.0", echo=True)
df.to_sql('elec2010', con=engine)
