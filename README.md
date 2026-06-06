# 🔐 Secure Password Kit

A Python command‑line tool that generates strong random passwords and checks the strength of any password you provide.

## ✨ Features

- ✅ Generate a secure password with a custom length (8–20 characters)
- ✅ Ensures each generated password contains:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character (`!@#$%^&*()`)
- ✅ Checks the strength of any password you enter (Weak / Medium / Strong)
- ✅ Displays generation rules and strength criteria
- ✅ Uses only the Python standard library (no external packages)

## 🚀 How to Run

1. Clone this repository or download `secure_password_kit.py`.
2. Make sure `validation.py` is in the same folder.
3. Open a terminal in the project folder and run:

```bash
python secure_password_kit.py
```

## 🛠️ Dependencies

· Python 3 (standard library only – no external packages)

## 📁 Files

· secure_password_kit.py – main program
· validation.py – helper module for numeric input validation (reused from other projects)

## 🔮 Future Improvements (Ideas Welcome)

· Save generated passwords to a file – Store the generated password and the date/time it was created (e.g., in a .txt or .json file) so you can retrieve previously generated passwords.


· Encrypt the saved passwords – Use a simple encryption method (e.g., basic XOR or base64) to protect stored passwords (for learning purposes only; real applications should use strong cryptography).


· Export password history – Allow the user to view, search, or delete old passwords from the saved file.


· Add a graphical user interface (GUI) – Using tkinter or a web interface with Flask.


· Custom character sets – Let the user choose which types of characters (uppercase, lowercase, digits, symbols) to include in the generated password.


· Password blacklist – Reject common or weak passwords (e.g., "password123") when checking strength.

## 💬 Feedback Welcome

I’m still learning, so any suggestions, code reviews, or ideas are highly appreciated.
Feel free to open an issue or contact me via GitHub.

---

Author: ```NaijaCodeClinician```


License: MIT

---
