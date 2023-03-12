# ChatgptOverWhatsApp

Hi, this is repository for connecting Twilio and OpenAI to provide answers to all the users questions using OpenAI ChatGpt. This is written in Python and served with Flask. This bot can only handle:

text messgaes



There are couple of things that you need before you get started following this repository.

OpenAI API key, since it is open to all, you can create an account here and access the key.
You need a Twilio project, you can get Account SID and Auth Token for that project, we will need this to make requests. You can get it from here. 
https://www.twilio.com/login?g=%2Fconsole-zen%2F&t=8106af639d51e0afc1a4286c23ba4b086f23c378c83bb122b84e6243152b669c

API requesting application like Postman, Insomnia, etc.
NGROK for local testing.
How to use it
To replicate the work of this repository and run it locally, you need to follow these steps:
```
create a .env file inside the root directory, create these environmental variables:
OPENAI_API_KEY=YOUR OPENAI API KEY
FROM=whatsapp:+14155238886

```


create a virtual environment and activate it before installing the packages
install all the required dependencies from the requirements.txt file
```
pip install -r requirements.txt
run the server with either of the following commands
python run.py
```

```
start NGROK engine on the same port as the python application is running.
provide the NGROk urlon Twilio WhatsApp Sandbox for all incoming request.
test the setup using your WhatsApp.
```
