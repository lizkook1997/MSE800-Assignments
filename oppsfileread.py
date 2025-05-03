import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

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

def load_cifar10_sample():
    print("\nLoading CIFAR-10 dataset...")
    (x_train, y_train), (_, _) = tf.keras.datasets.cifar10.load_data()
    print("CIFAR-10 sample shape:", x_train.shape)
    
    # Display the first two images with labels
    for i in range(2):  # 0 and 1
        plt.imshow(x_train[i])
        plt.title(f"Label: {y_train[i][0]}")
        plt.axis('off')
        plt.show()

def main():
    files = [
        "C:/Users/rishu/Downloads/Sample_data_2.parquet",
        "C:/Users/rishu/Downloads/sample_text.txt",
        "C:/Users/rishu/OneDrive/Desktop/MSE800-Assignments/sample_junk_mail.csv"
    ]

    for file in files:
        print(f"\nReading file: {file}")
        reader = DataReader(file)
        reader.read()
        reader.show_head(2)

    load_cifar10_sample()

# Entry point
if __name__ == "__main__":
    main()
