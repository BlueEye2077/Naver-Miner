# 📚 Naver Miner

A Python script/app to download chapters of a Manhua hosted on **Naver Webtoon**, using multithreading for fast performance and a stylish CLI interface with `rich` and `tqdm`.

---

## 🚀 Features

- 🚦 Terminal-based UI with rich banners and color output
- 🧵 Multi-threaded image downloads (via `ThreadPoolExecutor`)
- 📂 Automatically creates structured folders: `Downloaded Manhua/<title>/<chapter>`
- 🔍 BeautifulSoup-based HTML parsing
- 💥 Error handling and informative prompts

---

## 🛠️ Download

## Method 1:

- Download The `.exe` file and you're good to go


## Method 2:

- Install Python

- Install the requirments using:
  
```bash
pip install -r requirements.txt
```
- Run the script directly:

```bash
python main.py
```

## 🧬 How to use it?

After Launching The Script You’ll be prompted to enter the **chapter link** (e.g., a Webtoon episode URL). The script will:


1. Scrape the image URLs from the chapter.
2. Create the necessary folders.
3. Download all images concurrently.
4. Save them as `.jpg` files in the appropriate chapter folder.

Example folder structure:

```
Downloaded Manhua/
└── 12345(Manhua Id)/
    └── 12 (Chapter Number)/
        ├── 0.jpg
        ├── 1.jpg
        └── ...
```

---

## 📦 Requirements

- Python 3.7+
- Packages:
  - `requests`
  - `beautifulsoup4`
  - `tqdm`
  - `termcolor`
  - `rich`
  - `lxml`


---


## 📸 Screenshot


[![Screenshot-2025-06-14-215941.png](https://i.postimg.cc/vmWYxhJc/Screenshot-2025-06-14-215941.png)](https://postimg.cc/cKLyVR4S)
[![image.png](https://i.postimg.cc/4xfqQ5HY/image.png)](https://postimg.cc/SJPgycr4)

---

## ⚠️ Disclaimer

This tool is intended for educational or personal use only. Respect content ownership and do not use this tool for mass downloading or violating any site’s terms of service.

---

## 👨‍💻 Author

**BlueEye**  
💼 This project was crafted with love and threads.

---

## 📃 License

MIT License. See [LICENSE](LICENSE) for details.
