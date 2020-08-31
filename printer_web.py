from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/print', methods=['POST'])
def hello_world():
    req_data = request.get_json()
    encabezado = req_data['username']
    print encabezado
    return {"saludo":"Hello, World!"}

if __name__ == '__main__':
    app.run()
