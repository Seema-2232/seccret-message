import tkinter as tk
from tkinter import messagebox
from crypto_utils import generate_key, encrypt_message, decrypt_message

key = generate_key()

def encrypt():
    msg = entry.get()
    if not msg:
        messagebox.showwarning("Warning", "Enter a message")
        return
    encrypted = encrypt_message(msg, key)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, encrypted)

def decrypt():
    msg = entry.get()
    if not msg:
        messagebox.showwarning("Warning", "Enter encrypted text")
        return
    try:
        decrypted = decrypt_message(msg, key)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted)
    except:
        messagebox.showerror("Error", "Invalid key or encrypted text")

root = tk.Tk()
root.title("Secure Message Encryptor")
root.geometry("500x400")

tk.Label(root, text="Enter Message").pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

result_text = tk.Text(root, height=8, width=50)
result_text.pack(pady=10)

root.mainloop()