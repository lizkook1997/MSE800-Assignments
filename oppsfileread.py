import pandas as pd

class DataReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def read(self):
        if self.filepath.endswith('.parquet'):
            self.data = pd.read_parquet(self.filepath)
        elif self.filepath.endswith('.csv'):
            self.data = pd.read_csv(self.filepath)
        elif self.filepath.endswith('.txt'):
            self.data = pd.read_csv(self.filepath, header=None)
        else:
            raise ValueError("Unsupported file format")
        return self.data

    def show_head(self, rows=5):
        if self.data is not None:
            print(self.data.head(rows))
        else:
            print("No data loaded. Call read() first.")

# File paths
files = [
    "C:/Users/rishu/Downloads/Sample_data_2.parquet",
    "C:/Users/rishu/Downloads/sample_text.txt",
    "C:/Users/rishu/OneDrive/Desktop/MSE800-Assignments/sample_junk_mail.csv"  
]

# Read and show each file
for file in files:
    print(f"\nReading file: {file}")
    reader = DataReader(file)
    reader.read()
    reader.show_head(2)  
