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

posts = pd.read_csv('reddit-india-data-sample.csv')


#Applying text cleanup
posts['title'] = posts['title'].apply(TP.string_form)
posts['body'] = posts['body'].apply(TP.string_form)
posts['comment'] = posts['comment'].apply(TP.string_form)

posts['title'] = posts['title'].apply(TP.clean_text)
posts['body'] = posts['body'].apply(TP.clean_text)
posts['comment'] = posts['comment'].apply(TP.clean_text)

'''
	Various combinations of features were tried of which the combination of comments, body, url and title gave the best
	accuracy.(70 %)
'''
    
feature_combine = posts["title"] + posts["comment"] + posts["url"] +posts["body"]
posts = posts.assign(feature_combine = feature_combine)

'''
	Current combined features was stored in cleaned_dataset-3.csv. Various were combined and then tested against 
	different machine learning algorithms
'''

posts = pd.DataFrame(posts)
posts.to_csv('cleaned_dataset_title_comment__body_url.csv',index=False)
