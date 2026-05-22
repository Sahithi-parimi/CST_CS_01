# 🔐 Caesar Cipher Tool
### SkillCraft Technology — Task 01

---

## 📌 Project Description

The **Caesar Cipher Tool** is a command-line Python application that allows users to **encrypt** and **decrypt** text using the classic **Caesar Cipher algorithm** — one of the oldest and simplest encryption techniques in cryptography.

The Caesar Cipher works by shifting each letter of the alphabet by a fixed number of positions. For example, with a shift of 3:
- `A` → `D`
- `B` → `E`
- `HELLO` → `KHOOR`

Non-alphabetic characters (spaces, digits, punctuation) are left unchanged.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔒 Encrypt | Encrypt any plaintext message using a custom shift value (1–25) |
| 🔓 Decrypt | Decrypt an encrypted message if you know the shift value |
| 🔎 Brute-force | Try all 25 possible shifts at once to find the original message |
| 🔡 Case-preserving | Uppercase and lowercase letters are handled independently |
| 🛡️ Input validation | Handles invalid inputs gracefully |

---

## 📁 Project Structure

```
caesar_cipher/
│
├── caesar_cipher.py    # Main program file
└── README.md           # Project documentation
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system

### Steps

1. **Navigate to the project folder:**
   ```bash
   cd caesar_cipher
   ```

2. **Run the program:**
   ```bash
   python caesar_cipher.py
   ```
   > On some systems, use `python3` instead of `python`

3. **Follow the on-screen menu** to encrypt, decrypt, or brute-force a message.

---

## 💡 Example Usage

```
Enter your choice: 1
Enter the message to encrypt: Hello World
Enter shift value (1-25): 3

✅ Original Message : Hello World
   Shift Value      : 3
   Encrypted Text   : Khoor Zruog
```

```
Enter your choice: 2
Enter the message to decrypt: Khoor Zruog
Enter shift value (1-25): 3

✅ Encrypted Message : Khoor Zruog
   Shift Value       : 3
   Decrypted Text    : Hello World
```

---

## 🧠 Algorithm Explained

The Caesar Cipher shifts each letter by `n` positions in the alphabet:

- **Encryption:** `E(x) = (x + shift) mod 26`
- **Decryption:** `D(x) = (x - shift) mod 26`

Where `x` is the position of the letter (A=0, B=1, ..., Z=25).

---

## 📋 Commands Summary

| Command | Description |
|---|---|
| `python caesar_cipher.py` | Run on Windows |
| `python3 caesar_cipher.py` | Run on macOS/Linux |

---

*SkillCraft Technology — Task 01*
