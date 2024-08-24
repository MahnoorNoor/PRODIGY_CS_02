from PIL import Image
import numpy as np

# Function to encrypt the image using pixel value shifting
def shift_pixels(image_array, key):
    return np.mod(image_array.astype(np.int32) + key, 256).astype(np.uint8)

# Function to decrypt the image using pixel value shifting
def reverse_shift_pixels(image_array, key):
    return np.mod(image_array.astype(np.int32) - key, 256).astype(np.uint8)

# Function to encrypt the image by swapping pixels
def swap_pixels(image_array, key):
    np.random.seed(key)
    flat_image = image_array.flatten()
    shuffled_indices = np.random.permutation(flat_image.size)
    return flat_image[shuffled_indices].reshape(image_array.shape)

# Function to decrypt the image by reversing the pixel swap
def reverse_swap_pixels(image_array, key):
    np.random.seed(key)
    flat_image = image_array.flatten()
    shuffled_indices = np.random.permutation(flat_image.size)
    reverse_indices = np.argsort(shuffled_indices)
    return flat_image[reverse_indices].reshape(image_array.shape)

# Function to save the processed image
def save_image(image_array, output_path):
    Image.fromarray(image_array).save(output_path)
