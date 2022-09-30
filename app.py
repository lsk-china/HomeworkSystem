from flask import Flask
import advpymysql.core.processer as db

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    db.setConnectionData("connection.properties")
    app.run()
