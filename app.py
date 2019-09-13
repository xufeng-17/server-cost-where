from flask import Flask

from src.user.route import  apiLogin

app = Flask(__name__)


apiLogin(app)


if __name__ == '__main__':
    app.run()
