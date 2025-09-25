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
git clone https://github.com/your-username/web-brochure-builder.git
cd web-brochure-builder
