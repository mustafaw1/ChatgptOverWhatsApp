from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)
openai.api_key = ' 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'

def get_answere(question):
    #get the response back from the chatgpt
    completions = openai.Completion.create(
        model = 'text-davinci-003',   #ID of the model to use
        temperature = 0.5,            #what sampling temperature to use
        prompt = question,            #questions
        max_tokens = 100,             #size of the buffer actually
        n = 1,                        #how many completion generate from each prompt
        stop = None,                  #where the api stop generating further token
    )
    #fectch and return the text
    return completions.choices[0].text


@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    question = request.form.get('Body')
    print('User query: ', question)
    twilio_response = MessagingResponse()
    reply = twilio_response.message()
    #generate response using chatgpt
    answere = get_answere(question)
    # send back answere as a whatsapp reply
    reply.body(answere)
    #send the response back via whatsapp
    return str(twilio_response)


