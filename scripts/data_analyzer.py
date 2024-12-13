
import pandas
import matplotlib
from textblob import TextBlob
from summa import keywords

def analyze_sentiment(headline):
    analysis = TextBlob(headline)
    polarity = analysis.sentiment.polarity

    # Categorizing sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"




def extract_keywords(text):
    return keywords.keywords(text)