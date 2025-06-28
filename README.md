# 📧 VoMail: Voice-to-Email Assistant

**VoMail** is a voice-powered email assistant built by [Harsh Barot](https://github.com/harshisking), designed to let you speak naturally and send professional emails instantly. It’s built with local AI (Mistral via Ollama), works offline, and stores your contacts securely.

---

## 🎯 Features

- 🎤 **Voice Input**: Speak your command — like "Send an email to Riya"
- 🧠 **AI-Powered Email Generator**: Prompts are turned into polished emails using a local LLM
- 📇 **Smart Contacts**: Store and retrieve emails by alias
- 📤 **Instant Sending**: Automatically sends the generated email via SMTP
- 🔒 **Offline-first**: Designed for privacy, using open-source tools

---

## 🛠️ Tech Stack

- Python 3.10+
- `speech_recognition`
- `sqlite3`
- `smtplib`
- `Ollama` + `Mistral`
- `dotenv`
- `pytest` (for testing)

---

## 📂 Project Structure

```

VoMail/
├── core/
│   ├── speech.py
│   ├── contacts.py
│   ├── generate.py
│   ├── send.py
│   └── utils.py
├── models/
│   └── prompt_templates.json
├── db/
├── tests/
│   └── test_contacts.py
├── assets/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
└── .env

````

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/VoMail.git
cd VoMail
````

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file:

```env
EMAIL_ADDRESS=your-email@provider.com
EMAIL_PASSWORD=your-app-password
```

---

## ✅ Running Tests

Make sure you have `pytest` installed:

```bash
pip install pytest
```

Then run all tests from the root folder:

```bash
pytest
```

---

## 📜 License

This project is licensed under the MIT License:

```text
MIT License

Copyright (c) 2025 Harsh Barot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

> 💡 Built with love and local AI by Harsh Barot — to make email smarter, faster, and voice-driven.

