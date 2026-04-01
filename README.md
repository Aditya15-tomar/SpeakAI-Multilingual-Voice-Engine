# 🎙️ SpeakAI — Multilingual Voice Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TTS-XTTS%20v2-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/GSoC-2025%20Project-orange?style=for-the-badge&logo=google"/>
  <img src="https://img.shields.io/badge/Languages-7%2B-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge"/>
</p>

> **Speak once. Be heard in every language — naturally.**

A real-time, speech-to-speech translation engine that doesn't just convert words — it preserves the *feel* of your voice across Hindi, Arabic, Chinese, French, Spanish, German, and Japanese using state-of-the-art voice cloning and multilingual TTS.

---

## 🌍 Why I Built This

I've always been bothered by one thing: most TTS systems sound robotic the moment they step outside English. They handle Latin scripts okay, but throw Devanagari, Arabic, or Chinese at them and the pronunciation falls apart completely.

That gap matters. It means millions of people — Hindi speakers, Arabic speakers, Chinese speakers — are left with tools that mispronounce their language, which feels dismissive of their entire linguistic identity.

**SpeakAI is my attempt to fix that.** Not just by translating words, but by generating speech that *actually sounds right* — using voice cloning so the output feels personal, not synthetic.

This project was built as a GSoC contribution proposal to extend the [Speak-AI](https://github.com/Speak-AI) ecosystem with scalable, high-quality multilingual voice synthesis.

---

## ✨ What It Does

You speak into your mic. SpeakAI does everything else.

```
🎤  Your Voice
    ↓
🧠  Google Speech Recognition  →  Transcribed Text
    ↓
🌐  Language Detection
    ↓
🔄  Deep Translator            →  Translated Text (7 languages)
    ↓
🗣️  XTTS v2 + Voice Cloning   →  Natural Speech Output
    ↓
💾  output/ folder             →  One .wav file per language
```

It supports three modes:
- **`auto`** — translate and speak in all 7 supported languages at once
- **`translate`** — pick one specific target language
- **`multi`** — same as auto, but designed for batch multilingual workflows

---

## 🌐 Supported Languages

| Language | Code | Script |
|----------|------|--------|
| Hindi | `hi` | Devanagari |
| French | `fr` | Latin |
| Spanish | `es` | Latin |
| Arabic | `ar` | Arabic |
| Chinese (Simplified) | `zh` | Hanzi |
| German | `de` | Latin |
| Japanese | `ja` | Kanji / Hiragana |

> More languages are on the roadmap — see [Future Plans](#-future-plans).

---

## 🛠️ Tech Stack

| Component | Tool |
|-----------|------|
| Language | Python 3.9+ |
| TTS Engine | [Coqui TTS — XTTS v2](https://github.com/coqui-ai/TTS) |
| Speech Recognition | `SpeechRecognition` (Google API) |
| Translation | `deep-translator` (Google Translator) |
| ML Backend | PyTorch + Torchaudio |
| Voice Cloning | Reference audio (`voice.wav`) |
| Caching | Hash-based file existence check |

---

## 📦 Installation

Make sure you have Python 3.9+ and a working microphone.

```bash
# Clone the repo
git clone https://github.com/Aditya15-tomar/SpeakAI-Multilingual-Voice-Engine.git
cd SpeakAI-Multilingual-Voice-Engine

# Install dependencies
pip install -r requirements.txt
```

> **Note:** The XTTS v2 model is large (~1.8GB) and will be downloaded automatically on first run. Make sure you have a stable internet connection and enough disk space.

---

## 🚀 Usage

```bash
python main.py
```

You'll be guided through these steps:

1. **Speak** into your microphone when prompted
2. **Choose a mode** when asked:
   ```
   Mode (auto / translate / multi):
   ```
3. If you chose `translate`, pick your target language:
   ```
   Enter target language (hi, fr, es, ar, zh, de, ja):
   ```
4. Wait for the model to process — output `.wav` files appear in the `output/` folder, organized by language

```
output/
├── hindi/
│   └── hindi.wav
├── french/
│   └── french.wav
├── arabic/
│   └── arabic.wav
└── ...
```

---

## 📁 Project Structure

```
SpeakAI-Multilingual-Voice-Engine/
│
├── main.py              # Core pipeline — speech in, audio out
├── requirements.txt     # All dependencies
├── voice.wav            # Reference audio for voice cloning
├── output samples/      # Pre-generated demo outputs
├── .gitignore
└── README.md
```

---

## 🔬 The Core Challenge: Pronunciation

Translation is the easy part. **Pronunciation is where most systems fail.**

When you run Hindi text through a generic TTS, it often treats Devanagari like a foreign object — mispronouncing vowel matras, ignoring schwa deletion rules, and flattening the natural prosody of the language. Arabic gets its consonant clusters mangled. Chinese tones? Often completely ignored.

**What SpeakAI does differently:**

- Uses **XTTS v2**, a speaker-conditioned multilingual model trained on diverse scripts
- Applies **voice cloning** via `voice.wav` to maintain consistent voice identity across all languages
- Processes each language through its own TTS language token, so the model applies script-appropriate phoneme rules

**What's still being improved:**

- Grapheme-to-Phoneme (G2P) integration for more precise phoneme generation
- Schwa deletion for Hindi (a rule most models ignore)
- Tonal handling for Chinese
- Right-to-left script awareness for Arabic

This is an active research area — the current version works well, but pronunciation quality is something I'm deliberately prioritizing in the next iteration.

---

## ⚡ Performance

The first run is slow because XTTS v2 loads a ~1.8GB model. After that:

- **Caching** — if a `.wav` file already exists for a language, it's reused instantly
- **Single model load** — XTTS is loaded once and reused across all languages in a session
- Per-language generation time is logged to the console for benchmarking

Example timing (on a mid-range GPU):
```
Hindi  → ~4.2 sec
French → ~3.8 sec
Arabic → ~5.1 sec
Chinese → ~4.6 sec
```

---

## 🔮 Future Plans

This project is designed as a **foundation**, not a finished product. Here's what's coming next:

### Pronunciation & Quality
- [ ] Integrate G2P models (e.g., `phonemizer`) for phoneme-level accuracy
- [ ] Language-specific post-processing (schwa deletion for Hindi, tone marks for Chinese)
- [ ] Native speaker validation framework

### Model & Inference
- [ ] Benchmark XTTS v2 vs. Bark, MMS, and other open-source TTS models
- [ ] ONNX runtime export for faster, lighter inference
- [ ] Low-resource device optimization

### Language Expansion
- [ ] Brazilian Portuguese
- [ ] Swahili
- [ ] Bengali
- [ ] Kinyarwanda
- [ ] Quechua / Aymara (low-resource language exploration)

### Developer Experience
- [ ] REST API / WebSocket interface for real-time streaming
- [ ] Web UI for browser-based interaction
- [ ] Docker container for easy deployment

---

## 🧪 Sample Outputs

Pre-generated audio samples are available in the [`output samples/`](./output%20samples/) folder. These were generated from English input translated into all 7 supported languages using the default `voice.wav` reference.

---

## 🤝 Contributing

Contributions are very welcome — especially from native speakers of supported languages who can help validate pronunciation quality.

If you notice a mispronunciation or want to add a new language, feel free to open an issue or PR. There's no contribution too small.

```bash
# Fork the repo, make your changes, then:
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Open a Pull Request
```

---

## 📄 License

This project is licensed under the **MIT License** — use it, extend it, build on it.

---

## 👤 Author

**Aditya Singh Tomar**
- GitHub: [@Aditya15-tomar](https://github.com/Aditya15-tomar)
- Built as part of a GSoC 2025 project proposal

---

## 💬 A Note on What This Is Really About

I want to be clear about something: this isn't just a pipeline that chains a few APIs together.

The goal is to make speech technology feel *equal* across languages. Right now, if you're a Hindi speaker using a TTS tool, your language sounds like an afterthought. If you're an Arabic speaker, your script often gets mispronounced in ways that would make a native speaker wince.

SpeakAI is a step toward fixing that — starting with pronunciation, extending to more scripts, and eventually reaching languages that have almost no TTS support at all.

That's the real mission here. The code is just the beginning.
