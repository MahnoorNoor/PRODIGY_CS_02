
# Pixel Manipulation for Image Encryption

Pixel Manipulation for Image Encryption is a Python-based tool that allows users to encrypt and decrypt images using pixel manipulation techniques. This project provides a simple yet effective way to secure images by altering pixel values or shuffling their positions based on a secret key provided by the user.


## Features

- **Pixel Value Shifting:** Encrypts images by shifting the pixel values based on a key.
- **Pixel Swapping:** Randomly shuffles the pixel positions in the image to encrypt it.
- **User-Friendly GUI:** A Tkinter-based graphical user interface (GUI) that simplifies the process of encrypting and decrypting images.

## Project details


###  **Getting Started**
   **Prerequisites**


Make sure you have Python installed along with the following libraries:

- numpy
- Pillow (PIL)
- tkinter (usually included with Python)

You can install the necessary libraries using pip:

pip install numpy pillow


### **Usage:**

**Encryption:**

- Select an image file to encrypt.
- Choose the encryption method: "Shift Pixels" or "Swap Pixels".
- Enter a numeric key for encryption.
- Save the encrypted image to a desired location.

**Decryption:**

- Select an encrypted image file to decrypt.
- Choose the decryption method: "Shift Pixels" or "Swap Pixels".
- Enter the same numeric key used for encryption.
- Save the decrypted image to a desired location.

**Running the GUI**
To run the GUI application, execute the gui.py file:

python gui.py

### **Troubleshooting**

**Error: 256 integer out of bounds for uint8**

**Issue**

When working with pixel values in image processing, you may encounter an error indicating that 256 integer is out of bounds for uint8. This error occurs because pixel values are typically represented as 8-bit unsigned integers (uint8), which have a value range of 0-255. Any value outside this range will cause this error.

**Solution**

1. To address this issue, we used the **numpy.clip()** function to ensure that pixel values stay within the valid range of 0-255. Here’s how it was resolved in the code:

**Pixel Value Shifting:**
Updated the shift_pixels and reverse_shift_pixels functions to clip pixel values to the range of 0-255 using numpy.clip.

2. **Code Changes:**

- def shift_pixels(image_array, key):
    return np.clip((image_array + key) % 256, 0, 255).astype(np.uint8)

- def reverse_shift_pixels(image_array, key):
    return np.clip((image_array - key) % 256, 0, 255).astype(np.uint8)

    By using **np.clip()**, pixel values are constrained to the 0-255 range, preventing the out-of-bounds error and ensuring the image processing functions work correctly.



### **How to Use**

### Clone the Repository:

 git clone https://github.com/MahnoorNoor/PRODIGY_CS_02.git

### Navigate to the Project Directory:

cd pixel-manipulation-encryption





## Acknowledgements

- Thanks to the open-source community for providing the libraries and tools used in this project.
- Special thanks to the  reviewers who provided valuable feedback.