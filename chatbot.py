import random
import json
import torch
# import pypyodbc as odbc
import torch.nn as nn
import os
import sys
# from prompt_data_base import conn

from main import tokenize, bag_of_words
from model import NeuralNet

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


with open("intents.json",'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "UNIVERSITY CHATBOT"




def get_response(msg):
    sentence = tokenize(msg)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()].strip()

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]


    

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                responses = intent['responses']
                non_empty_resposnses = [response for response in responses if response.strip()]
                if non_empty_resposnses:
                    response = random.choice(non_empty_resposnses)
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    print(f"Bot Response: {response}")
                    return response , prob.item(), tag

    response = "I'm not sure what you're asking . Can you please rephrase?"
    print(f"Bot Response: {response}")
    return response , prob.item(), tag if tag else None 



    # else:
    #     print("Low confidence prediction")
    #     response = "I'm not sure what you're asking. Can you please rephrase?"
    #     print(f"Bot Response: {response}")
    #     return response , prob.item() , tag









