from tkinter import Tk, Label, Button, Entry, filedialog, Radiobutton, StringVar, messagebox
import numpy as np
from PIL import Image
import os

# Import the core functions
from image_encryption import shift_pixels, reverse_shift_pixels, swap_pixels, reverse_swap_pixels, save_image

# Set the fixed directory path
fixed_directory = r"C:\Users\User\Desktop\Pixel Manupulation for image Encryption"

# Function to perform the encryption or decryption based on user input
def process_image(operation):
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("PNG files", "*.png")])
    if not image_path:
        return

    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Invalid Input", "Key must be an integer.")
        return

    key = int(key)
    method = method_var.get()

    try:
        image_array = np.array(Image.open(image_path))

        if operation == 'encrypt':
            if method == 'shift':
                processed_array = shift_pixels(image_array, key)
            elif method == 'swap':
                processed_array = swap_pixels(image_array, key)
            output_filename = "encrypted_image.png"
            output_message = "Image Encrypted and Saved!"
        elif operation == 'decrypt':
            if method == 'shift':
                processed_array = reverse_shift_pixels(image_array, key)
            elif method == 'swap':
                processed_array = reverse_swap_pixels(image_array, key)
            output_filename = "decrypted_image.png"
            output_message = "Image Decrypted and Saved!"

        # Save the image to the fixed directory
        output_path = os.path.join(fixed_directory, output_filename)
        save_image(processed_array, output_path)
        messagebox.showinfo("Success", output_message + f"\nSaved at {output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the GUI
root = Tk()
root.title("Pixel Manipulation for Image Encryption")
root.geometry("500x400")

Label(root, text="Enter your key:").pack(pady=10)
key_entry = Entry(root)
key_entry.pack(pady=10)

method_var = StringVar(value='shift')

Radiobutton(root, text="Shift Pixels", variable=method_var, value='shift').pack(pady=5)
Radiobutton(root, text="Swap Pixels", variable=method_var, value='swap').pack(pady=5)

Button(root, text="Encrypt Image", command=lambda: process_image('encrypt')).pack(pady=10)
Button(root, text="Decrypt Image", command=lambda: process_image('decrypt')).pack(pady=10)

root.mainloop()
