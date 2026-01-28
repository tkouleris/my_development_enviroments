

import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

load_dotenv()

def create_app():

    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')    
    return app


app = create_app()
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)



@app.route("/")
def hello_world():    
    return "Hello World!!!!"

@app.route("/api/test", methods=["POST"])
def test():
    data = request.json
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    ) 