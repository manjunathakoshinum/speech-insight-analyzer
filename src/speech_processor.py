import os
import wave
import json
from vosk import Model, KaldiRecognizer

def transcribe_audio(wav_path, model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Vosk model not found at: {model_path}")

    wf = wave.open(wav_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Input must be mono PCM WAV.")

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, wf.getframerate())
    recognizer.SetWords(True)

    plain_text = ""
    word_timestamps = []

    while True:
        data = wf.readframes(4000)
        if not data:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            plain_text += result.get('text', '') + " "
            word_timestamps.extend(result.get('result', []))

    final_result = json.loads(recognizer.FinalResult())
    plain_text += final_result.get('text', '')
    word_timestamps.extend(final_result.get('result', []))

    if not plain_text.strip():
        print("Warning: Empty audio or no speech detected.")

    return plain_text.strip(), word_timestamps