Speak-AI Multilingual Voice System
Overview :-

This project is an enhanced multilingual version of the Speak-AI system, designed to convert speech into natural-sounding voice outputs across multiple languages. The main focus is not just translation, but high-quality pronunciation and accessibility.

The system takes live speech input, detects the language, translates it (if needed), and generates speech output using a modern multilingual TTS model.

Motivation

Most existing TTS systems support limited languages or produce unnatural pronunciation, especially for non-Latin scripts like Hindi, Arabic, or Chinese.

This project aims to:

Break language barriers 
Improve pronunciation quality 
Support real-time multilingual communication
 Features
 Speech-to-Text using microphone input
 Automatic Language Detection
 Real-time Translation
 Multilingual Text-to-Speech (TTS)
 Voice Cloning using reference audio (voice.wav)
 Caching System to avoid recomputation
 Supports multiple languages:
Hindi (hi)
French (fr)
Spanish (es)
Arabic (ar)
Chinese (Simplified) (zh-cn)

 System Architecture

 Microphone Input
        ↓
 Speech Recognition (Google API)
        ↓
 Language Detection
        ↓
 Translation (Deep Translator)
        ↓
XTTS (Multilingual Voice Synthesis)
        ↓
 Output Audio Files

 Tech Stack
Python
Coqui TTS (XTTS v2)
SpeechRecognition
Deep Translator
PyTorch / Torchaudio

 Installation

pip install -r requirements.txt

  Usage

python main.py

Steps:
Speak into your microphone 
Choose mode:
auto → default language output
translate → one selected language
multi → multiple languages
Audio files will be generated in the output/ folder

 Project Structure
suger/
│── main.py
│── requirements.txt
│── README.md
│── voice.wav
│── output/
How It Works
Captures voice input using microphone
Converts speech to text using Google Speech Recognition
Detects source language
Translates text into target languages
Uses XTTS model for realistic speech generation
Saves output audio files
Uses hashing-based caching to improve performance
 Focus on Pronunciation Quality

Pronunciation is the core focus of this project.

Current approach:

Uses speaker-conditioned XTTS for natural voice output
Maintains consistency across languages using voice cloning

Planned improvements:

Integration of Grapheme-to-Phoneme (G2P) systems
Better handling of:
Devanagari (Hindi)
Arabic script
Chinese tonal pronunciation
 Performance Optimization
Implemented caching to avoid repeated audio generation
Reduced redundant model inference
Measured generation time for each language

 Future Work

This project is designed as a foundation for deeper research and improvements:

- Pronunciation Improvements
Integrate G2P models for accurate phoneme generation
Language-specific pronunciation tuning
- Model Exploration
Compare XTTS with other open-source TTS models
Evaluate quality vs performance trade-offs
- Performance Enhancements
ONNX runtime integration
Faster inference on low-resource devices
- Evaluation Framework
Native speaker validation
Language-wise pronunciation benchmarking
- Extended Language Support
Portuguese (Brazilian)
Swahili
Quechua / Aymara
Kinyarwanda

 Community & Validation

Future iterations will include:

Feedback from native speakers
Iterative improvements based on real-world usage
Community-driven language validation
 Sample Outputs

Generated audio files are stored in:

output/

Each file corresponds to translated speech in a different language.

 Why This Project Matters
Improves accessibility for multilingual users
Helps in language learning
Supports inclusive communication
Bridges gap between speech and understanding

 Author

Aditya Singh Tomar

 Final Note

This project is not just about converting text to speech —
it is about making speech sound natural, accurate, and accessible across languages.