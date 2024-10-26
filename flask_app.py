from flask import Flask

app = Flask(__name__)

def home():
    return "<p>Hello world!</p>"

if __name__ == '__main__':
    app.run(debug=True)