import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # return your index.html here!
    pass

@app.route("/auth")
def authorize():
    # return your auth URL here!
    pass


if __name__ == '__main__':
    app.run(host="localhost", port="8000", debug=True)
