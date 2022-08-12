import pickle
import pandas as pd
import re

model_path = r'././Lib/model/'

with open(model_path+ 'RandomForest.pickle', 'rb') as handle:
    model = pickle.load(handle)

def predict_data(data_input):
    D = pd.DataFrame([data_input])
    result = model.predict(D)[0]
    return [result]


