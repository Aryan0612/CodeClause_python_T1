import random
import string
import tkinter as tk

def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title('Random Password Generator')

length_label = tk.Label(root, text='Password Length:')
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text='Generate Password', command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

password_label = tk.Label(root, text='Password:')
password_label.grid(row=2, column=0, padx=5, pady=5)

password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
