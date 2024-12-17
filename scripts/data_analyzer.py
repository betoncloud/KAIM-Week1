
import pandas
import matplotlib
from textblob import TextBlob
from summa import keywords
import pandas as pd
import pytz

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

def convert_mixed_datetime(value):
    if pd.isna(value):        
        return None
    try:
        dt = pd.to_datetime(value)  # Convert to datetime
        if dt.tzinfo is None:       # If naive, make it timezone-aware (e.g., UTC)
            return dt.replace(tzinfo=pytz.UTC)        
        return dt  # Return as-is if already timezone-aware
    except Exception as e:       
        print(f"Error parsing value: {value}, {e}")
        return None
    
def calculate_rsi(data, window=7):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi