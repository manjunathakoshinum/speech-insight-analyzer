# 📢 Speech Insight Analyzer

> **Why?**
> This tool transforms **raw audio** into **emotion-aware transcripts** to help speakers, content creators, and educators analyze, reflect, and grow.

---

## ⚡ Introduction

**Speech Insight Analyzer** is a lightweight, modular Python tool designed to:

* 🎙️ Transcribe `.wav` audio using **Vosk** (lightweight, offline speech-to-text engine)

* 😃 Detect emotions at the word level using **HuggingFace Transformers**

* 📊 Assign an "impact score" to help evaluate public speaking delivery

* 🎯 Save structured output for further processing (e.g., generating videos from audio)

Built initially on **18th Dec 2024**, this tool was optimized for fast, offline usage in Colab and local environments.

---

# 🧭 Step One of a Larger Vision

This project is Step One of a more advanced speech insight system.

While this version is built in Python for fast prototyping and public sharing, a more powerful and extensible version is currently being developed privately in Java, designed to include:

🎙️ Real-time voice analysis

🧠 Advanced emotional impact scoring

📈 Progress tracking and feedback loop

🕺 Integration of voice

---

## 📚 Table of Contents

1. [Why Vosk?](#why-vosk)
2. [Installation](#installation)
3. [How It Works](#how-it-works)
4. [Usage](#usage)
5. [Folder Structure](#folder-structure)
6. [Output Examples](#output-examples)
7. [Limitations](#limitations)
8. [Future Work](#future-work)

---

## 🔥 Why Vosk?

Vosk is:

* ✅ **Lightweight** (runs on CPU, even on Raspberry Pi)

* 🚀 **Fast** transcription engine

* 📴 **Offline** — no internet needed once the model is downloaded

* 🎯 Perfect for **WAV mono PCM audio** transcription

---

## 📂 Try It Now

You can run the notebook directly in Google Colab:

[👉 Click here to open Colab](https://colab.research.google.com/drive/11bVoELFBvSFEou-KfPiK4nmac1-rE53g?usp=sharing)

---

## ⚙️ Installation

### 🔌 Core Dependencies

```bash
pip install vosk
pip install soundfile
apt-get install -y ffmpeg
pip install transformers torch nltk requests
```

### 📦 Download Vosk Model (Example for English)

```bash
mkdir -p /content/drive/MyDrive/vosk_models
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip \
     -O /content/drive/MyDrive/vosk_models/vosk-model-small-en-us-0.15.zip
unzip /content/drive/MyDrive/vosk_models/vosk-model-small-en-us-0.15.zip \
      -d /content/drive/MyDrive/vosk_models/
```

### 📁 Model Path

Update your code:

```python
model_path = "/content/drive/MyDrive/vosk_models/vosk-model-small-en-us-0.15"
```

---

## 🚀 How It Works

1. Converts `.mp3` or `.m4a` to `.wav` via `ffmpeg`

2. Transcribes `.wav` to text with timestamps using Vosk

3. Detects emotions using HuggingFace `distilroberta-base`

4. Scores word-level impact

5. Saves all output to `/output/` folder

---

## 🧪 Usage

### 🎯 Run from CLI:

```bash
python main.py --audio path/to/input.mp3 --model path/to/vosk-model
```

### 📁 Output:

* `output/yourfile_plain.txt` → plain transcription

* `output/yourfile_timestamps.txt` → words with timestamps

* `output/yourfile_emotions.json` → emotions + impact scores

---

## 🗂️ Folder Structure

```
speech-insight-analyzer/
├── main.py
├── requirements.txt
├── models/                  # (ignored in .gitignore)
├── output/                  # auto-generated outputs
├── src/
│   ├── speech_processor.py  # Vosk-based transcription
│   ├── emotion_analyzer.py  # HuggingFace emotion scoring
│   └── export_utils.py      # file-saving logic
└── README.md
```

---

## 🧾 Output Examples

### 📄 Plain Transcription:

```
this is your final test audio input without any punctuation needed
```

### 🕐 Timestamp Log:

```
this: [0.42s - 0.60s]
is: [0.61s - 0.75s]
your: [0.76s - 0.93s]
...
```

### 💥 Emotions JSON:

```json
[
  {
    "word": "great",
    "start": 2.41,
    "end": 2.91,
    "impact_score": 0.76,
    "emotion": "joy"
  }
]
```

---

## ⚠️ Limitations

* Only supports **mono WAV audio** for transcription

* No punctuation or sentence boundary detection

* One language per model (no multilingual support)

* Internet required for HuggingFace emotion model

---

## 🌱 Future Work

* ✅ Java version with GUI (planned) and extended features

* ✅ Streamlit app for real-time speaking practice

* 🔄 Add sentence boundary detection

* 📊 Dashboard for progress review and emotion tracking

---

## ✨ Author

Built by **\[Manjunata H]** with ❤️

---

## 📧 Contact & Contributions

* 📩 **Email:** [Reach out here](manjunathakoshinum@gmail.com)

* 🌟 If you found this useful, **please give it a star!**

* 🤝 Want to improve it? Feel free to **submit a pull request** — though note:

  > ⚠️ I am **not actively maintaining the Python version**, as the project is being further developed in **Java**.

* 💼 [Connect on LinkedIn](https://www.linkedin.com/in/manjunathah)

---
