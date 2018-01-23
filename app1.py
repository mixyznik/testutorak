"""Flask app."""

from flask import Flask
from models import Comment

app = Flask(__name__)

UM = UserManager('.csv')


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
    table = UM.table()
    return page.format(table)