from typing import List
import re
import string
import spacy
from spacy.lang.nb.stop_words import STOP_WORDS


nlp = spacy.load("nb_core_news_sm")
stopwords = list(STOP_WORDS)


def spacy_tokenizer(text: str) -> List[str]:
    """
    Tokenizes the input text and returns a list of tokens:
        - clean text
        - lemmatize
        - lower case
        - remove stopwords
    """
    tokens = nlp(clean_text(text))
    tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_
              for word in tokens]
    tokens = [word for word in tokens if word not in stopwords]
    return tokens


def clean_text(text: str) -> str:
    """
    Removes numbers and punctuations from the text.
    """
    # Remove numbers
    cleaned = re.sub(r"\d+", "", text)

    # Remove punctuations
    cleaned = "".join([char for char in cleaned if char not in string.punctuation])

    return cleaned
