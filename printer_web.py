from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/print')
def hello_world():
    return {"saludo":"Hello, World!"}

if __name__ == '__main__':
    app.run()
