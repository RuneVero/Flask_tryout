from flask import Flask

app = Flask(__name__)

def home():
    return "<p>Welkom bij mijn Flask-applicatie!</p>"

if __name__ == '__main__':
    app.run(debug=True)