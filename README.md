# ⚡ Python Task Automation Suite (GUI Application)

A desktop GUI automation tool built using Python and Tkinter to streamline daily file management and data parsing workflows.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Key Features

- **📷 Image Organizer (`.jpg` / `.jpeg`)**:
  - Automatically scans a source folder and moves all JPG images to a designated target folder.
  - Keeps non-image files untouched.

- **✉️ Email Extractor (`.txt`)**:
  - Parses text files using Regex to find all email patterns (`user@domain.com`).
  - Removes duplicate entries and saves unique emails to a output `.txt` file.

- **🖥️ User-Friendly GUI**:
  - Tabbed window interface built with Tkinter.
  - Native file dialog pickers for quick folder/file selection.

---

## 🛠️ Tech Stack & Concepts

- **GUI Interface**: `tkinter`, `ttk`, `filedialog`, `messagebox`
- **File & OS Operations**: `pathlib`, `shutil`
- **Data Parsing & Extraction**: `re` (Regular Expressions)

---

## 🚀 How to Run

### Option 1: Run via Python
Make sure Python 3.8+ is installed on your machine.

```bash
python gui_app.py