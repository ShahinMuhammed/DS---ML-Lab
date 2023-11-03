import pandas as pd
orders=pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user')
print("overview of dataframe: ")
print(orders.head())
print("Shape:",orders.shape)
user_cols=['user_id','age','gender','occupation','zip_code',]
users=pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user',sep='|',header=None,names=user_cols)
print("Dataframes after modifying the default parameter values for read_table:")
print(users.head())
