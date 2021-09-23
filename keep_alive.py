from flask import Flask
from threading import Thread

#Keeps bot alive
app = Flask('')

@app.route('/')
def home():
    return "<h3>Bot is online!</h3>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()