#!/usr/bin/env bash
set -ef
rm -rf $(pipenv --venv)
pipenv install

# NLP downloads for the environment
pipenv run python -m spacy download en_core_web_sm
pipenv run python -m spacy download nb_core_news_sm
pipenv run python -c "import nltk;nltk.download('punkt');nltk.download('stopwords')"
