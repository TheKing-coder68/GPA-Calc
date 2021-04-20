from flask import Flask
from login.login import login
from main.home import home_blueprint
import os
app = Flask(__name__)
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(home_blueprint, url_prefix="/home")
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', None)


if __name__=="__main__":
    app.run(debug=True)
