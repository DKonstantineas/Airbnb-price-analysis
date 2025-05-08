import pandas as pd


df_calendar = pd.read_csv(r'Data/Athens(airbnb)/calendar.csv')

print(df_calendar.isna().sum())
# count=0
# for index, value in df_calendar:
#     print(value)
#     if index is None:
#         count=count+1
# print(count)