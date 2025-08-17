import os
from sre_parse import Tokenizer
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np

with open("intents.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer=pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder=pickle.load(encoder_file)

while True:
    input_text = input("Enter your command-> ")
    padded_sequences = pad_sequences(
        tokenizer.texts_to_sequences([input_text]),
        maxlen=20,
        truncating='post'
    )
    result = model.predict(padded_sequences)
    tag = label_encoder.inverse_transform([np.argmax(result)])[0]  # ✅ String now

    for intent in data['intents']:
        if intent['tag'] == tag:
            print(np.random.choice(intent['responses']))
            break  # Stop after finding the first match
