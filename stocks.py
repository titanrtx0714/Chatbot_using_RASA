import requests
import pandas as pd
import json
import flair
import regex as re
sentiment_model = flair.models.TextClassifier.load('en-sentiment')

def get_data(tweet):
    data = {
        'id': tweet['id_str'],
        'created_at': tweet['created_at'],
        'text': tweet['full_text']
    }
    return data

def clean(tweet):
    whitespace = re.compile(r"\s+")
    web_address = re.compile(r"(?i)http(s):\/\/[a-z0-9.~_\-\/]+")
    user = re.compile(r"(?i)@[a-z0-9_]+")
    # we then use the sub method to replace anything matching
    tweet = whitespace.sub(' ', tweet)
    tweet = web_address.sub('', tweet)
    tweet = user.sub('', tweet)
    return tweet


def stock_analysis(ticker):
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAFW9QAEAAAAAnOQAdHMvdF3L0Bc6g8reSOpPAtg%3D5OvcbaeX2HoXqlhzQdtkVImgjwPLDmvYmYRMMcP2QXAUHNVVLf'
    params = {
        'q': ticker,
        'tweet_mode': 'extended',
        'lang': 'en',
        'count': '100'
    }

    response = requests.get(
        'https://api.twitter.com/1.1/search/tweets.json', params=params,
        headers={
            'authorization': 'Bearer ' + BEARER_TOKEN
        })

    df = pd.DataFrame()
    for tweet in response.json()['statuses']:
        row = get_data(tweet)
        df = df.append(row, ignore_index=True)

    # we will append probability and sentiment preds later
    probs = []
    sentiments = []

    # use regex expressions (in clean function) to clean tweets
    df['text'] = df['text'].apply(clean)

    # sentiment_model = flair.models.TextClassifier.load('en-sentiment')
    for tweet in df['text'].to_list():
        # make prediction
        sentence = flair.data.Sentence(tweet)
        sentiment_model.predict(sentence)
        # extract sentiment prediction
        probs.append(sentence.labels[0].score)  # numerical score 0-1
        sentiments.append(sentence.labels[0].value)  # 'POSITIVE' or 'NEGATIVE'

    # add probability and sentiment predictions to tweets dataframe
    df['probability'] = probs
    df['sentiment'] = sentiments

    if(len(df)!=0):
        counts = df['sentiment'].value_counts().to_dict()

        for key, value in counts.items():
            if (key == 'POSITIVE'):
                positives = int(value / len(df) * 100)
            if (key == 'NEGATIVE'):
                negatives = int(value / len(df) * 100)

        message = ""
        message += ("Here's what people are saying about " + ticker + ":" + "\n" "POSITIVE: " + str(positives) + "%" + "\n" "NEGATIVE: " + str(negatives) + "%")

        return message

    else:
        return "Sorry your request could not be completed."



