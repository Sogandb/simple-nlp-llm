import pandas as pd

texts = [
    "I love this product!",
    "I am sad today.",
    "It was an amazing experience!",
    "This is bad."
]

df = pd.DataFrame({"text": texts})

# تحلیل احساسی ساده (rule-based)
def simple_sentiment(text):
    positive_words = ["love", "good", "amazing", "happy"]
    negative_words = ["bad", "sad", "angry"]

    score = 0
    for w in positive_words:
        if w in text.lower():
            score += 1
    for w in negative_words:
        if w in text.lower():
            score -= 1

    return "positive" if score > 0 else "negative"

df["sentiment"] = df["text"].apply(simple_sentiment)

print(df)