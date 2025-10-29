# train_sentiment_model.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# 1️⃣ Create a tiny training dataset
data = {
    "text": [
        "I love football",
        "This game is awesome",
        "What a terrible match",
        "I hate losing",
        "Our team played great",
        "That was an awful performance"
    ],
    "sentiment": ["positive", "positive", "negative", "negative", "positive", "negative"]
}

df = pd.DataFrame(data)

# 2️⃣ Build a simple pipeline model
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# 3️⃣ Train the model
model.fit(df["text"], df["sentiment"])

# 4️⃣ Save it
joblib.dump(model, "sentiment_model.pkl")

print("✅ Sentiment model trained and saved as 'sentiment_model.pkl'")