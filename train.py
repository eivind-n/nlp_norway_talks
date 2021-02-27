import pandas as pd
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

from preprocess import spacy_tokenizer
from utils import configure_pandas


DATAPATH = "./data/raw/data/"


def main() -> None:
    """
    Trains a party_name classifier based on text count features.
    """
    configure_pandas()

    df = pd.read_csv(f"{DATAPATH}ton.csv", low_memory=False)

    # Remove outlier text lengths
    df = df[df["text"].str.len() < 3000]

    # Only keep full records of party_name and text
    df = df[["party_name", "text"]].dropna(how="any")
    print(f"{len(df)} full records.")

    # Limit dataset for faster iterations during testing
    # N = 10000
    # df = df.loc[:N, :]

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["party_name"],
        test_size=0.3,
        random_state=1,
        stratify=df["party_name"])

    # Encode targets based on train
    target_encoder = LabelEncoder()
    target_encoder.fit(y_train)
    y_train = target_encoder.transform(y_train)
    y_test = target_encoder.transform(y_test)

    # Features + model pipeline
    pipeline = Pipeline(
        [
            ("vect", TfidfVectorizer(
                tokenizer=spacy_tokenizer,
                analyzer="word",
                max_df=0.9,
                min_df=5,
                ngram_range=(1, 2)
            )),
            ("clf", XGBClassifier()),
        ]
    )

    # Train
    pipeline.fit(X_train, y_train)

    # Measure on test set
    y_pred = pipeline.predict(X_test)
    print(metrics.classification_report(y_test, y_pred, target_names=target_encoder.classes_))

    # TODO grid search, hyperparameters, etc.


if __name__ == "__main__":
    main()
