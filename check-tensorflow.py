import tensorflow as tf
import matplotlib.pyplot as plt

# Load the MNIST dataset (example)
mnist = tf.keras.datasets.mnist

# Load the training images and labels
(train_images, train_labels), (_, _) = mnist.load_data()

# Display the first image from the training set
plt.imshow(train_images[0], cmap='gray')  # The data is grayscale
plt.axis('off')
plt.title("First MNIST Image")
plt.show()
