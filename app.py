import gradio
#from transformers import pipeline

#username = "yrajm1997"
#repo_name = "finetuned-sentiment-model"
#repo_path = username+ '/' + repo_name
#sentiment_model = pipeline(model= repo_path)

# Function for response generation
def predict_sentiment(text):
    
    return text

# Input from user
in_prompt = gradio.components.Textbox(lines=10, placeholder=None, label='Enter review text')

# Output response
out_response = gradio.components.Textbox(type="text", label='Sentiment')

# Gradio interface to generate UI link
title = "Sentiment Classification"
description = "Analyse sentiment of the given review"

iface = gradio.Interface(fn = predict_sentiment,
                         inputs = [in_prompt],
                         outputs = [out_response],
                         title = title,
                         description = description)

iface.launch(server_name = "0.0.0.0", server_port = 8001) # Ref. for parameters: https://www.gradio.app/docs/interface
