import tkinter as tk
from tkinter import ttk
import secrets
import string

def generate_password(length=12, chars=None):
    if chars is None:
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("David's Password Generator")
        self.geometry("400x250")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = ttk.Label(self, text="Secure Password Generator", font=("Segoe UI", 16))
        title_label.pack(pady=10)

        # Password length selection
        length_frame = ttk.Frame(self)
        length_frame.pack(pady=5)

        length_label = ttk.Label(length_frame, text="Password length:")
        length_label.pack(side=tk.LEFT, padx=5)

        self.length_var = tk.IntVar(value=12)
        self.length_slider = ttk.Scale(length_frame, from_=4, to=64, orient=tk.HORIZONTAL, variable=self.length_var)
        self.length_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Generate button
        generate_btn = ttk.Button(self, text="Generate Password", command=self.generate_password_action)
        generate_btn.pack(pady=10)

        # Password display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(self, textvariable=self.password_var, font=("Consolas", 12), state="readonly", width=40)
        password_entry.pack(pady=5)

        # Copy button
        copy_btn = ttk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)

    def generate_password_action(self):
        length = int(self.length_var.get())
        password = generate_password(length)
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            self.update()  # Keeps the copied password even after app is closed
            self.show_copied_message()

    def show_copied_message(self):
        # Temporary status message
        copied_label = ttk.Label(self, text="Password copied to clipboard!", foreground="green")
        copied_label.pack()
        self.after(2000, copied_label.destroy)  # Auto-remove after 2 seconds

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
