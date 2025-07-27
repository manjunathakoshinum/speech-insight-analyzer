from transformers import pipeline

SIGNIFICANT_EMOTIONS = {"joy", "surprise", "anger", "sadness", "fear"}

try:
    emotion_classifier = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=True
    )
except Exception as e:
    emotion_classifier = None
    print("Error loading emotion model. Check your internet connection.")

def analyze_word_emotions(word_entries, threshold=0.5):
    if emotion_classifier is None:
        print("Emotion model unavailable. Skipping emotion analysis.")
        return []

    high_impact = []
    for entry in word_entries:
        word = entry["word"]
        try:
            scores = emotion_classifier(word)
        except Exception as e:
            continue

        emotions = scores[0]
        impact_score = sum(e["score"] for e in emotions if e["label"] in SIGNIFICANT_EMOTIONS)
        top_emotion = max(emotions, key=lambda x: x["score"])["label"]

        if impact_score > threshold:
            high_impact.append({
                "word": word,
                "start": entry["start"],
                "end": entry["end"],
                "impact_score": round(impact_score, 3),
                "emotion": top_emotion
            })

    return high_impact