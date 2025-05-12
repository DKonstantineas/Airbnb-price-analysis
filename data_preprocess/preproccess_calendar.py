import pandas as pd
import numpy as np

# # Read the CSV file
# df_calendar = pd.read_csv('Data/Athens(airbnb)/calendar.csv')

# # Replace NaN values with None for MySQL compatibility
# df_calendar = df_calendar.where(pd.notnull(df_calendar), None)

# # Alternatively, use this approach to replace NaN with None:
# # df_calendar = df_calendar.applymap(lambda x: None if pd.isna(x) else x)

# # Check the DataFrame to ensure NaN values are now None
# print(df_calendar.head())



# df_listings = pd.read_csv('Data/Athens(airbnb)/listings.csv')
# print(df_listings.to_string().encode('utf-8').decode('utf-8'))
# import pandas as pd

# # Attempt to load the file with proper handling for complex CSVs
# df = pd.read_csv(
#     'Data/Athens(airbnb)/listings.csv',
#     encoding='utf-8',                # or try 'utf-8-sig' or 'ISO-8859-1' if you get encoding errors
#     quotechar='"',
#     escapechar='\\',
#     on_bad_lines='skip',             # or 'warn' to diagnose problematic rows
#     engine='python'                  # better with complex CSVs than C engine
# )
# print(df)


# Load the CSV
df = pd.read_csv('Data/Athens(airbnb)/calendar.csv')

# Clean price columns (remove $ and convert to float)
for col in ['price', 'adjusted_price']:
    df[col] = df[col].replace(r'[\$,]', '', regex=True).astype(float)

# Replace NaN with None for SQL compatibility
df = df.where(pd.notnull(df), None)

df['adjusted_price']='None'

print(df.head().to_string())