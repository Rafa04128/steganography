import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import stepic  # Make sure stepic is installed

def encode_image(img, msg):
    encoded = stepic.encode(img, msg.encode())
    return encoded

def decode_image(img):
    decoded = stepic.decode(img)
    return decoded

def upload_action():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
    if img_path:
        status_label.config(text="Image Uploaded Successfully")

def encrypt_action():
    if img_path and password_entry.get():
        img = Image.open(img_path)
        encoded_img = encode_image(img, password_entry.get())
        encoded_img.save('encoded_image.png')
        status_label.config(text="Image Encoded and Saved as 'encoded_image.png'")
    else:
        messagebox.showerror("Error", "Please upload an image and enter a password")

def decrypt_action():
    if img_path:
        img = Image.open(img_path)
        password = decode_image(img)
        status_label.config(text=f"Decoded Password: {password}")
    else:
        messagebox.showerror("Error", "Please upload an encoded image")

# Tkinter GUI setup
root = tk.Tk()
root.title("Steganography App")

upload_button = tk.Button(root, text="Upload Image", command=upload_action)
upload_button.pack()

password_entry = tk.Entry(root, width=50)
password_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_action)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_action)
decrypt_button.pack()

status_label = tk.Label(root, text="", wraplength=300)
status_label.pack()

# Start the GUI event loop
root.mainloop()
