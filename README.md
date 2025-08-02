

# 🔐 GUI Password Generator in Python (Tkinter)

A sleek, user-friendly desktop application that allows you to generate **secure passwords** with customizable lengths. Built using Python’s `tkinter` library and powered by the `secrets` module for cryptographically strong randomization.

---

## 🖥️ Features

- ✅ Graphical User Interface (GUI) with modern styling
- 🔢 Adjustable password length (4 to 64 characters)
- 🔐 Uses `secrets` for strong, random password generation
- 📋 One-click copy to clipboard
- 🚀 Lightweight, fast, and standalone — no external dependencies

---


---

## 📦 Requirements

- Python 3.6+
- No third-party libraries needed — uses built-in:
  - `tkinter`
  - `secrets`
  - `string`

---

## 💡 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/gui-password-generator.git
cd gui-password-generator
Run the App

bash
Copy
Edit
python gui_password_gen.py
📸 Features at a Glance
Feature	Description
🎚️ Adjustable Length	Choose between 4–64 characters
🔒 Secure Generation	Uses Python's secrets module
📋 Copy to Clipboard	Instantly copies password to system clipboard
🎨 Simple GUI	Clean, responsive layout using tkinter

✨ Example Use Case
Creating strong passwords for:

Online accounts

Wi-Fi credentials

Secure vaults

Developer keys / tokens

🛠️ To Customize
You can adjust character sets used in the generate_password() function:

python
Copy
Edit
chars = string.ascii_letters + string.digits + string.punctuation
For example, exclude punctuation:

python
Copy
Edit
chars = string.ascii_letters + string.digits

