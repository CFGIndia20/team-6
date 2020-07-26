import keras
from keras.models import load_model
import pandas as pd
import numpy as np
dico = {}

from nltk.corpus import stopwords
import nltk
# nltk.download('stopwords')

from textblob import Word
# nltk.download("wordnet")

import pickle
file_handle = open("T:\\cfg\\github\\team-6\\app\\templates\\tokenizer" , "rb")

tokenizer = pickle.load(file_handle)

class_dict = {1:"Certificates" , 2:"Crime and Safety" , 3:"Electricity and Power Supply" , 4:"Fire Safety" , 
 5:"Garbage and Unsanitary Practices" , 6:"Lakes" , 7:"Others" , 8:"Pollution" , 9:"Mobility - Roads, Footpaths and Infrastructure" , 
 10:"Storm Water Drains" , 11:"Animal Husbandry" , 12:"Traffic and Road Safety" , 13:"Parks & Recreation" , 
 14:"Water Supply and Services" , 15:"Public Transport - BMTC" , 16:"Public Transport - KSRTC" ,17:"Railways" ,
 18:"Community Infrastructure and Services" , 19:"Public Toilets" , 20:"Playgrounds" , 21:"Streetlights" , 
 22:"Sewerage Systems" , 23:"Trees and Saplings"}


def get_standard_dictionary(path):
	
	dico1 = open(path)
	for word in dico1:
		word = word.split()
		dico[word[0]] = word[1]
	dico1.close()

	return dico

def txt_std(words):
    list_words = words.split()
    for i in range(len(list_words)):
        if list_words[i] in dico.keys():
            list_words[i] = dico[list_words[i]]
    return ' '.join(list_words)

def preprocess(text):
	df = pd.DataFrame([text])

	df = df.loc[0].apply(lambda x: ' '.join([i.lower() for i in x.split()]))
	df = df.str.replace(r'[^\w\s]',"")

	dico = get_standard_dictionary("emnlp_dict.txt")
	
	df = df.apply(txt_std)
	df = df.str.replace(r"xx+\s","")


	stop = stopwords.words('english')
	df =df.apply(lambda x: ' '.join([i for i in x.split() if i not in stop]))

	df = df.apply(lambda x:' '.join([Word(i).lemmatize() for i in x.split()]))
	
	seq = tokenizer.texts_to_sequences(df.values)

	print(seq)

	return seq

def get_prediction(model , text):
	input_vector = preprocess(text)

	prediction = model.predict(input_vector)

	pred_class = np.argmax(prediction)
	print("PREDICTION")
	print(class_dict[pred_class])


	# print(prediction)


def load_lstm_model(path):
	model = load_model(path)
	return model	


def main_predict(text):
	model_path = "T:\\cfg\\github\\team-6\\app\\templates\\model.h5"
	model = load_lstm_model(model_path)
	return get_prediction(model, text)

if __name__ == "__main__":
	model_path = "model.h5"

	# preprocess("Hi there.")
	model = load_lstm_model(model_path)
	get_prediction(model , "We are facing multiple issues related to road safety some of them include the \nRoad being dug out but never repaired making it extremely dangerous for pedestrain and kids as vehicle move close by")

	# print(model)

