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



# Properly read complex CSV
df = pd.read_csv(
    'Data/Athens(airbnb)/listings.csv',
    encoding='utf-8'        # Use 'utf-8-sig' if BOM errors happe
)

for col in df.columns:
    df[col] = df[col].apply(lambda x: ' '.join(x.split()) if isinstance(x, str) else x)


# Print a summary, not full table
#print(df.info())
print(df.head(5))  # Sample 2 rows
print(df['host_id'])
df.to_csv(path_or_buf='Data\Athens(airbnb)\check.csv', sep=',')


# # Load the CSV
# df = pd.read_csv('Data/Athens(airbnb)/calendar.csv')

# # Clean price columns (remove $ and convert to float)
# for col in ['price', 'adjusted_price']:
#     df[col] = df[col].replace(r'[\$,]', '', regex=True).astype(float)

# # Replace NaN with None for SQL compatibility
# df = df.where(pd.notnull(df), None)

# df['adjusted_price']='None'

# print(df.head().to_string())
