#!/usr/bin/env bash
set -ef
rm -rf $(pipenv --venv)
pipenv install

# pytorch install works with pip -f, but fails with pipenv (ubuntu 20.04)
pipenv run pip install torch==1.7.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html

# NLP downloads for the environment
pipenv run python -m spacy download en_core_web_sm
pipenv run python -m spacy download nb_core_news_sm
pipenv run python -c "import nltk;nltk.download('punkt');nltk.download('stopwords')"
