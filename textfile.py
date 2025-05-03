# import pandas as pd

# # Read the text file as a single-column dataframe
# df = pd.read_csv('"C:\Users\rishu\Downloads\sample_text.txt"')

# # Print lines 1 and 2 (index 0 and 1)
# print(df.iloc[0])
# print(df.iloc[1])

import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('C:\\Users\\rishu\\Downloads\\sample_text.txt')

# Print the top two rows
print(df.head(2))
