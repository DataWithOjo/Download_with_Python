# 🐍 Exercise 1 – Downloading and Extracting Files with Python

This project is part of a series of hands-on exercises designed to improve your Python and data engineering skills. In **Exercise 1**, you will download zipped CSV files from HTTP URLs using Python, extract them, and organize them programmatically within a containerized environment.

---

## 📋 Problem Statement

Write a Python script that performs the following:

- ✅ Creates a folder named `downloads/` if it doesn't exist.
- 📥 Downloads 10 ZIP files from specified HTTP URLs.
- 🧩 Extracts the original filename from each URL.
- 🗃️ Unzips each file to extract the `.csv` inside.
- 🧹 Deletes the ZIP file after extraction.
- ⚠️ Handles invalid or broken URLs gracefully.
- ⭐ *(Bonus)*: Try using `aiohttp` for async downloads, `ThreadPoolExecutor` for parallelization, and write unit tests.

---

## ⚙️ Setup Instruct

`docker-compose up run`
