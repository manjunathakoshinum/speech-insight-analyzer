import os
import argparse
import logging
import subprocess
from src.speech_processor import transcribe_audio
from src.emotion_analyzer import analyze_word_emotions
from src.export_utils import save_plain_text, save_timestamps, save_emotion_json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_audio_to_wav(input_path, output_path):
    logging.info("Converting audio to WAV format using ffmpeg...")
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", input_path,
            "-ac", "1", "-ar", "16000",
            output_path
        ], check=True)
        logging.info("Conversion successful.")
    except subprocess.CalledProcessError as e:
        logging.error("FFmpeg conversion failed. Ensure ffmpeg is installed.")
        raise

def main():
    parser = argparse.ArgumentParser(description="Speech Insight Analyzer")
    parser.add_argument("--audio", required=True, help="Path to audio file (wav/mp3/m4a)")
    parser.add_argument("--model", required=True, help="Path to Vosk model folder")
    args = parser.parse_args()

    base_name = os.path.splitext(os.path.basename(args.audio))[0]
    wav_path = f"temp_{base_name}.wav" if not args.audio.endswith(".wav") else args.audio

    if not args.audio.endswith(".wav"):
        convert_audio_to_wav(args.audio, wav_path)

    try:
        text, word_data = transcribe_audio(wav_path, args.model)
        impact_words = analyze_word_emotions(word_data)

        save_plain_text(text, f"output/{base_name}_plain.txt")
        save_timestamps(word_data, f"output/{base_name}_timestamps.txt")
        save_emotion_json(impact_words, f"output/{base_name}_emotions.json")

        logging.info("✅ Processing complete. Files saved in 'output/' folder.")
    except Exception as e:
        logging.error(f"❌ Error: {e}")
    finally:
        if wav_path.startswith("temp_") and os.path.exists(wav_path):
            os.remove(wav_path)

if __name__ == "__main__":
    main()