# 📦 Exercise 1: Download and Extract Data from HTTP Source

This project demonstrates a simple yet essential data engineering task: programmatically downloading a dataset from an HTTP source, extracting the contents, and preparing it for analysis or processing.

## ✅ What This Project Does

- 📥 Downloads a ZIP file from a public HTTP URL
- 📂 Extracts the contents using Python's built-in libraries
- 🗃️ Saves the extracted files to a designated directory
- 📌 Handles basic error scenarios like failed downloads or corrupted archives

---

## 🔧 Tools & Libraries

- Python 3.7+
- `requests` – to download files over HTTP
- `zipfile` – to extract `.zip` archives
- `os` & `pathlib` – for filesystem operations

---

## 🚀 How to Run

1. **Clone this repository**

2. **Install requirements** (optional, only if you use a `requirements.txt` file):

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:

    ```bash
    python main.py
    ```

    The script will:
    - Create a `data/` directory if it doesn't exist
    - Download the file from the specified HTTP URL
    - Extract its contents into the `data/` directory

---

