from nltk.corpus.reader.reviews import Review
from pydantic import BaseModel

# The only input we need is the text that a review may write about a movie
class request_body(BaseModel):
    review: str