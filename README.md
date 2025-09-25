# Web Brochure Builder using LLM

Automatically generate a company brochure from a website using GPT and web scraping.

This tool scrapes the landing page and key subpages (like "About", "Careers", etc.) from a company website, extracts the relevant content, and generates a concise brochure using OpenAI's GPT models.

![Gradio UI](https://img.shields.io/badge/Powered%20by-Gradio-%23FF6B00?style=flat&logo=gradio)
![OpenAI](https://img.shields.io/badge/API-OpenAI-%2300A67E)

---

## 🚀 Features

- 🧠 Uses GPT to summarize company content.
- 🌐 Scrapes landing page + relevant subpages.
- 📄 Generates a marketing-style brochure in **Markdown**.
- 🖼️ Gradio interface for easy usage.
- 🔒 Keeps API keys secure using `.env` file.

---

## 📦 Requirements

- Python 3.7+
- OpenAI API key (GPT-4 access recommended)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/capi20/Web_Brochure_GenAI.git
cd Web_Brochure_GenAI
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Create a .env file in the root of the project:

```bash
# .env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Usage
Run the app with:

```bash
python main.py
```

This will launch a Gradio web interface in your browser.

### ✍️ Input:
- **Company Name** – for display in the brochure
- **Website URL** – full URL including `https://`

### 📄 Output:
- A formatted **Markdown brochure** with:
  - Company overview
  - Culture highlights
  - Careers info (if available)
  - Contact or mission statement (if available)

## 🧠 How It Works

1. Scrapes the main landing page.
2. Uses GPT to pick relevant subpages (like "About", "Careers").
3. Scrapes selected pages.
4. Sends combined content to GPT with instructions to generate a brochure.
5. Streams the result live in the browser.

## ✅ Example Use Cases

- Quickly generate investor-ready summaries.
- Automatically create company briefs from new websites.
- Help recruiters or researchers understand a company from its site.


