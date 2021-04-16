from flask import Flask
from login.login import login
import os
app=Flask(__name__)
app.register_blueprint(login, url_prefix="/login")
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', None)

@app.route('/')
def test():
    return "TEST"

if __name__=="__main__":
    app.run(debug=True)
