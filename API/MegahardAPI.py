import json
from flask import *
from SpotifyAPI import SpotifyTrackGrabber

app = Flask(__name__)

"""
POST
"""

"""
GET
"""


@app.route('/songinput/<string:song>', methods=['GET'])
def getsong(song):
    song_id = SpotifyTrackGrabber.search_for_track(SpotifyTrackGrabber, song)

    SpotifyTrackGrabber.set_track_in_queue(SpotifyTrackGrabber, song_id)


@app.route('/currentqueue', methods=['GET'])
def getqueue():
    queue = SpotifyTrackGrabber.get_queue(SpotifyTrackGrabber)
    artist = queue['item']['artists'][0]['name']
    song = queue['item']['name']

    return jsonify({'artist': artist, 'song': song})


"""
PUT
"""

"""
DELETE
"""
if __name__ == "__main__":
    app.run(debug=True)
