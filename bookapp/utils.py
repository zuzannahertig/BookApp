import pandas as pd
from transformers import pipeline
import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt 
from scipy.interpolate import make_interp_spline
from io import BytesIO
import urllib, base64

def read_novel(path):
   
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        novel = f.read().replace('\r', ' ').replace('\n', ' ')

    return novel


model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path, max_length=512, truncation=True)


def get_labels(complete_scores):
    list_of_scores = []
    for i in complete_scores:
        list_of_scores.append(i[0].get('label'))

    return list_of_scores

def change_values(labels, sentences):

    df = pd.DataFrame(sentences, columns = ['sentence'])
    df['score'] = labels
    df = df.replace({'score' : { 'positive' : 1, 'negative' : 0, 'neutral' : 0.5 }})

    return df

def paa(arr, sections):
    try:
        assert arr.shape[0] != sections
    except AssertionError as e:
        return np.copy(arr)
    else:
        sectionarr = np.zeros(sections)
        space_size = np.arange(0, arr.shape[0] * sections - 1)
        outputIndex = space_size // arr.shape[0]
        inputIndex = space_size // sections
        uniques, nUniques = np.unique(outputIndex, return_counts=True)
        
        res = [arr[indices].sum() / arr.shape[0] for indices in
                np.split(inputIndex, nUniques.cumsum())[:-1]]

    return res

def paa_values(df, length):
    y = df['score']  
    y.reset_index(drop=True, inplace=True)
    y = pd.DataFrame(y)

    y = y.transpose()
    y = np.array(y).flatten()

    return paa(y, length)

def data_to_cluster(df, length=10):

    val = paa_values(df, length=length)

    return val

def smooth(series, length):

    x = np.array(list(range(length)))
        
    x_y_spline = make_interp_spline(x, series)
    y_ = np.linspace(x.min(), x.max(), 100)
    x_ = x_y_spline(y_)

    return x_, y_

def transform_data(series, length):
    smoothed = [smooth(x, length) for x in series]

    return [smoothed[x][0] for x in range(len(smoothed))]

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(x, y):
    plt.switch_backend('AGG')
    # fig = plt.figure()
    plt.plot(x, y)
    plt.axis('off')
    plt.tight_layout()
    chart = get_graph()
    return chart

def get_image(df, length=6):
    series = data_to_cluster(df, length)
    s = smooth(series, length)
    x = s[1]
    y = s[0]
    chart = get_chart(x, y)

    return chart

def generate_image(text):
    sentences = sent_tokenize(text)
    complete_score = [sentiment_task(sentence) for sentence in sentences]
    labels = get_labels(complete_score)
    df = change_values(labels, sentences)
    image = get_image(df, 6)
    return image 