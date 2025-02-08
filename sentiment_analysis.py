import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
reviews_df = pd.read_csv("reviews.csv")

# Ensure there are no missing reviews
reviews_df = reviews_df.dropna(subset=['Review'])

# Clean the text by removing special characters (basic text preprocessing)
reviews_df['CleanedReview'] = reviews_df['Review'].str.replace(r'[^a-zA-Z\s]', '', regex=True).str.lower()

# Label creation for sentiment analysis (assuming rating > 3 is positive, <= 3 is negative)
reviews_df['Sentiment'] = np.where(reviews_df['Rating'] > 3, 'Positive', 'Negative')

# Vectorize text using TF-IDF for efficient and effective text representation
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(reviews_df['CleanedReview'])

# Target labels
y = reviews_df['Sentiment']

# Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training: Naive Bayes for text classification
model = MultinomialNB()
model.fit(X_train, y_train)

# Model Prediction
y_pred = model.predict(X_test)

# Performance Metrics
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

# Print metrics to the console
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(json.dumps(report, indent=2))

# Aggregate Sentiment Analysis Insights
positive_reviews = int((y_pred == 'Positive').sum())
negative_reviews = int((y_pred == 'Negative').sum())

# Save insights to a JSON file for the dashboard
sentiment_data = {
    "accuracy": float(accuracy),
    "positive_reviews_count": positive_reviews,
    "negative_reviews_count": negative_reviews
}

with open("sentiment_analysis_results.json", "w") as json_file:
    json.dump(sentiment_data, json_file, indent=4)

print("Sentiment analysis results have been saved to sentiment_analysis_results.json.")
