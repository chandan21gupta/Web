'''
	This script was used to clean the data for its processing. It was used to removing special characters, spacing, and irrelevant 
	words such as "a","the" etc using nltk library in python.
	The text cleaning function was derived form the module textcleaning.py
'''

import logging
import pandas as pd
import numpy as np
from numpy import random
import gensim
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import textcleaning as TP

topics_data = pd.read_csv('reddit-india-data-sample.csv')


#Applying text cleanup
topics_data['title'] = topics_data['title'].apply(TP.string_form)
topics_data['body'] = topics_data['body'].apply(TP.string_form)
topics_data['comment'] = topics_data['comment'].apply(TP.string_form)

topics_data['title'] = topics_data['title'].apply(TP.clean_text)
topics_data['body'] = topics_data['body'].apply(TP.clean_text)
topics_data['comment'] = topics_data['comment'].apply(TP.clean_text)

'''
	Various combinations of features were tried of which the combination of comments, body, url and title gave the best
	accuracy.(70 %)
'''
    
feature_combine = topics_data["title"] + topics_data["comment"] + topics_data["body"] + topics_data["url"] 
topics_data = topics_data.assign(feature_combine = feature_combine)

'''
	Current combined features was stored in cleaned_dataset-3.csv. Various were combined and then tested against 
	different machine learning algorithms
'''

topics_data = pd.DataFrame(topics_data)
topics_data.to_csv('cleaned_dataset-3.csv',index=False)
