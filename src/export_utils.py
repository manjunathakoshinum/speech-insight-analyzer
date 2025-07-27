import json
import os

def save_plain_text(text, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text.strip())

def save_timestamps(word_entries, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for w in word_entries:
            f.write(f"{w['word']}: [{w['start']:.2f}s - {w['end']:.2f}s]\n")

def save_emotion_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)