# TORTURA DO BOT: Dá um choque periódico nele, pra evitar que ele durma.
# Inspiração: https://www.youtube.com/watch?v=nMSXM3awDQ8

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Tô vivo, eu, tô"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()