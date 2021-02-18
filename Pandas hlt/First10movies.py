import pandas as pd 

movies_data = pd.read_csv("Movie-Data.csv", index_col ="Rank")
print(movies_data.loc[[1]])
print(movies_data.loc[[2]])
print(movies_data.loc[[3]])
print(movies_data.loc[[4]])
print(movies_data.loc[[5]])
print(movies_data.loc[[6]])
print(movies_data.loc[[7]])
print(movies_data.loc[[8]])
print(movies_data.loc[[9]])
print(movies_data.loc[[10]])
