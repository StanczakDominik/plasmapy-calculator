from flask import Flask

# Declare the app
app = Flask(__name__)

from application import routes
