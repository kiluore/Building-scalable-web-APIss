import joblib
from string import punctuation
from typing import Dict, List
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re 

# load our trained model as a global variable
global model
model = joblib.load("./models/sentiment_ml_pipeline.pkl")

# function to preprocess & cleaning the data received from a client request
def text_cleaning(text:str, remove_stop_words=True, lemmatize_words=True) -> List[str]:
    """
    A python function to preprocess incoming text data from a client request. 
    This function performs the basic text preparation steps used in natural language processing.

    Args:
        text (str): A string containing a corpus of text.
        remove_stop_words (bool, optional): Remove stop words from the text. Defaults to True.
        lemmatize_words (bool, optional): lemmatize words to their stem. Defaults to True.

    Returns:
        List[str]: A sanitized list of words to be used by the sentiment model
    """
 
    # Clean the text using regular expressions
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"http\S+", " link ", text) # remove any web related links
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)  # remove numbers

    # Remove punctuation from text using list comprehension
    text = "".join([c for c in text if c not in punctuation])

    # Optionally, remove stop words
    if remove_stop_words:

        # load stopwords
        stop_words = stopwords.words("english")
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)

    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)

    # Return a list of words
    return text

def predict_sentiment(review: str) -> Dict:
    """
    A simple function that receive a review content and predict the sentiment of the content.
    :param review:
    :return: prediction, probabilities
    """
    # clean the review
    cleaned_review = text_cleaning(review)

    # perform prediction
    prediction = model.predict([cleaned_review])
    output = int(prediction[0])
    probas = model.predict_proba([cleaned_review])
    output_probability = "{:.2f}".format(float(probas[:, output]))

    # output dictionary
    sentiments = {0: "Negative", 1: "Positive"}

    # show results
    result = {"prediction": sentiments[output], "probability": output_probability}
    return result