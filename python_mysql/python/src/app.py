from flask import Flask, jsonify
import MySQLdb
import os

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "mysql"),
    "user": os.getenv("MYSQL_USER", "myuser"),
    "passwd": os.getenv("MYSQL_PASSWORD", "mypass"),
    "db": os.getenv("MYSQL_DATABASE", "mydb"),
    "port": int(os.getenv("MYSQL_PORT", 3306)),
}

def get_db_connection():
    return MySQLdb.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        passwd=DB_CONFIG["passwd"],
        db=DB_CONFIG["db"],
        port=DB_CONFIG["port"],
        charset="utf8mb4",
    )

@app.route("/")
def hello_world():
    conn = get_db_connection()
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')