import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import stepic

def encode_image(img, msg):
    encoded = stepic.encode(img, msg.encode())
    return encoded

def decode_image(img):
    decoded = stepic.decode(img)
    return decoded

def upload_action():
    global img_path, img_preview
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
    if img_path:
        img = Image.open(img_path)
        img = img.resize((250, 250))
        img_preview = ImageTk.PhotoImage(img)
        preview_label.config(image=img_preview)
        status_label.config(text="Image Uploaded Successfully")

def encrypt_action():
    combined_message = password_entry.get() + ' ' + date_entry.get() + ' ' + info_entry.get()
    if img_path and combined_message.strip():
        img = Image.open(img_path)
        encoded_img = encode_image(img, combined_message)
        encoded_img.save('encoded_image.png')
        status_label.config(text="Image Encoded and Saved as 'encoded_image.png'")
    else:
        messagebox.showerror("Error", "Please upload an image and enter the required information")

def decrypt_action():
    if img_path:
        img = Image.open(img_path)
        decoded_message = decode_image(img)
        status_label.config(text=f"Decoded Message: {decoded_message}")
    else:
        messagebox.showerror("Error", "Please upload an encoded image")

# Tkinter GUI setup
root = tk.Tk()
root.title("Steganography App")
root.geometry("400x600")  # Adjusted for additional fields

button_style = {'font': ('Helvetica', 12), 'bg': '#4CAF50', 'fg': 'white'}

upload_button = tk.Button(root, text="Upload Image", command=upload_action, **button_style)
upload_button.pack(pady=10)

preview_label = tk.Label(root)
preview_label.pack(pady=10)

password_entry = tk.Entry(root, width=30, font=('Helvetica', 12))
password_entry.pack(pady=10)

date_entry = tk.Entry(root, width=30, font=('Helvetica', 12))
date_entry.pack(pady=10)

info_entry = tk.Entry(root, width=30, font=('Helvetica', 12))
info_entry.pack(pady=10)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_action, **button_style)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_action, **button_style)
decrypt_button.pack(pady=10)

status_label = tk.Label(root, text="", wraplength=300)
status_label.pack(pady=10)

root.mainloop()
