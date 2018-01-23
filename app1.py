"""Flask app."""

from flask import Flask
from models import Comment

app = Flask(__name__)

# UM = UserManager('.csv')


@app.route("/")
def index():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>NAAB</title>
    </head>

    <body>
        {}
    </body>

    </html>
    """
    message = 'Welcome'
    return page.format(message)

# @app.route("/")
#     def view():