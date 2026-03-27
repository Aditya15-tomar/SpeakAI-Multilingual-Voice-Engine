from TTS.api import TTS
import speech_recognition as sr
from deep_translator import GoogleTranslator
import os
import time

# 🎤 Initialize
r = sr.Recognizer()

# 📁 Base output folder
BASE_DIR = "output"
os.makedirs(BASE_DIR, exist_ok=True)

# 🎤 Take speech input
with sr.Microphone() as source:
    print("🎤 Speak...")
    audio = r.listen(source)

# 🔤 Speech to text
try:
    text = r.recognize_google(audio)
    print("🗣 You said:", text)
except Exception as e:
    print("❌ Could not understand audio:", e)
    exit()

# 🌍 Language detection (simple fallback)
detected_lang = "en"
print("🌍 Detected language:", detected_lang)

# 🔧 Language mappings
TRANSLATE_LANG_MAP = {
    "hi": "hi",
    "fr": "fr",
    "es": "es",
    "ar": "ar",
    "zh": "zh-CN",
    "de": "de",
    "ja": "ja"
}

TTS_LANG_MAP = {
    "hi": "hi",
    "fr": "fr",
    "es": "es",
    "ar": "ar",
    "zh": "zh-cn",
    "de": "de",
    "ja": "ja"
}

# 📁 Language full names (for folders)
LANG_NAME = {
    "hi": "hindi",
    "fr": "french",
    "es": "spanish",
    "ar": "arabic",
    "zh": "chinese",
    "de": "german",
    "ja": "japanese"
}

# 🎯 Mode selection
mode = input("Mode (auto / translate / multi): ").strip().lower()

if mode == "auto":
    target_languages = ["hi", "fr", "es", "ar", "zh", "de", "ja"]

elif mode == "translate":
    lang = input("Enter target language (hi, fr, es, ar, zh, de, ja): ").strip()
    target_languages = [lang]

elif mode == "multi":
    target_languages = ["hi", "fr", "es", "ar", "zh", "de", "ja"]

else:
    print("⚠ Invalid mode, using multi")
    target_languages = ["hi", "fr", "es", "ar", "zh", "de", "ja"]

# 🔊 Load TTS model once
print("🔄 Loading TTS model...")
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

# 🔁 Process languages
for lang in target_languages:
    try:
        print(f"\n🌍 Translating to {lang}...")

        translated_text = GoogleTranslator(
            source='auto',
            target=TRANSLATE_LANG_MAP.get(lang, "en")
        ).translate(text)

        print("➡ Translated:", translated_text)

    except Exception as e:
        print(f"❌ Translation failed for {lang}:", e)
        continue

    # 📁 Create language folder
    lang_folder = os.path.join(BASE_DIR, LANG_NAME.get(lang, lang))
    os.makedirs(lang_folder, exist_ok=True)

    # 📄 Clean filename
    filename = f"{LANG_NAME.get(lang, lang)}.wav"
    filepath = os.path.join(lang_folder, filename)

    if os.path.exists(filepath):
        print(f"⚡ Cached audio used for {lang}")
        continue

    try:
        start = time.time()

        tts.tts_to_file(
            text=translated_text,
            file_path=filepath,
            speaker_wav="voice.wav",
            language=TTS_LANG_MAP.get(lang, "en")
        )

        end = time.time()

        print(f"✅ {lang} audio saved → {filepath}")
        print(f"⏱ Time: {round(end - start, 2)} sec")

    except Exception as e:
        print(f"❌ TTS failed for {lang}:", e)

print("\n🎉 All done! Check 'output/' folder.")