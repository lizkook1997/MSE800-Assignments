import pandas as pd

# Read the Parquet file
df = pd.read_parquet('C:/Users/rishu/Downloads/Sample_data_2.parquet')

# Print the full DataFrame
print(df)

# Or print just the first few rows
print(df.head(0 ))
