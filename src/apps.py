from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

app = Flask(__name__)
api = swagger.docs(
    Api(app), apiVersion='0.1',
    basePath="http://localhost:5000/api/v0/",
    description="docs for data explorer api")


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=8000)
