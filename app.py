from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
from settings import DEFAULT_OPENAPI_REPLY
import os
from dotenv import load_dotenv

app = Flask(__name__)
openai.api_key = os.getenv('openai.api_key')
# conig()

def configure():
    load_dotenv


def get_answer(question):
    try:
        # get the response back from the chatgpt
        completions = openai.Completion.create(
            model = 'text-davinci-003',   #ID of the model to use
            temperature = 0.5,            #what sampling temperature to use
            prompt = question,            #questions
            max_tokens = 100,             #size of the buffer actually
            n = 1,                        #how many completion generate from each prompt
            stop = None,                  #where the api stop generating further token
        )
    except:
        return DEFAULT_OPENAPI_REPLY

    #fetch and return the text
    return completions.choices[0].text


@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    question = request.form.get('Body')
    print('User query: ', question)
    twilio_response = MessagingResponse()
    reply = twilio_response.message()

    #generate response using chatgpt
    answere = get_answer(question)
    # send back answere as a whatsapp reply
    reply.body(answere)
    #send the response back via whatsapp
    return str(twilio_response)


