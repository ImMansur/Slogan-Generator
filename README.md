## 🎯 Marketing Slogan Generator

A simple Python-based application that generates **marketing slogans** using **Azure OpenAI**, with support for multiple tones through external prompt templates.

---

## 🚀 Features

* Generate slogans using Azure OpenAI
* Supports multiple tones:

  * Professional
  * Friendly
  * Bold
* Prompt templates stored as `.txt` files
* Easy to extend with new tones
* Environment-variable based configuration

---

## 🛠️ Setup

```bash
git clone https://github.com/ImMansur/Marketing-Slogan-Generator.git
cd Marketing-Slogan-Generator
pip install openai python-dotenv
```

---

## ▶️ Run

```bash
python src/slogan_generator.py
```

You’ll be prompted to select a tone:

```
Available tones: professional, friendly, bold
Select tone:
```

---

## ✏️ Customization

### Change Product & Audience

Edit in `slogan_generator.py`:

```python
product_name = "Smart Fitness Watch"
target_audience = "Young professionals"
```

### Add a New Tone

1. Add a new prompt file in `prompts/`
2. Register it in the `prompts` dictionary

---

## 🌐 API Used

Azure OpenAI

---

## 📂 Storage

Prompt templates are stored in:

```
prompts/
```

Sample outputs are stored in:

```
examples/sample_output.txt
```

---

## 👤 Author

**Mansur**
GitHub: [https://github.com/ImMansur](https://github.com/ImMansur)

---