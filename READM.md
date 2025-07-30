# ✅ CodeAlpha Task 3 – Secure Coding Review

## 🔐 Project: Secure Python Login Authentication System

This project demonstrates a basic command-line login system using Python, with a focus on identifying and fixing common security vulnerabilities.

---

## 📝 Original Vulnerabilities (Before Fixes)

| # | Vulnerability | Description | Severity | Fix |
|---|---------------|-------------|----------|-----|
| 1 | Plaintext Password Storage | Stored passwords in plaintext in `users.txt` | High | Switched to SHA-256 hashing |
| 2 | No Input Validation | No checks on user input | Medium | Used `.strip()` and validation |
| 3 | No Brute-force Protection | Unlimited login attempts | High | Added 3-attempt limit |
| 4 | Hardcoded File Path | Assumes file is in same folder | Low | Can be improved with `os.path` |

---

## 🔧 Fixes Implemented

- ✅ Passwords are now hashed with SHA-256.
- ✅ Input is stripped to remove unwanted characters.
- ✅ Users get only 3 login attempts.
- ✅ Secure coding practices applied.

---

## 📦 File Structure

