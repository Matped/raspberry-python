import json
from flask import *
from SpotifyAPI import *

app = Flask(__name__)

"""
POST
"""


@app.route('/queuesong/<string:song_id>', methods=["POST"])
def queue_song(song_id):
    SpotifyTrackGrabber.set_track_in_queue(song_id)


"""
GET
"""


@app.route('/getplaylist', methods=['GET'])
def get_playlist():
    return jsonify(playlist)


@app.route('/songinput/<string:song>', methods=['GET'])
def get_song(song):
    track = SpotifyTrackGrabber.search_for_track(song)
    track_id = track['tracks']['items'][0]['uri']
    track_artist = track['tracks']['items'][0]['artists'][0]['name']
    track_name = track['tracks']['items'][0]['name']

    return jsonify({'id': track_id, 'artist': track_artist, 'name': track_name})


@app.route("/currentlyplaying", methods=['GET'])
def get_currently_playing():
    currently_playing = SpotifyTrackGrabber.currently_playing()
    artist = currently_playing['item']['artists'][0]['name']
    song = currently_playing['item']['name']
    duration_ms = currently_playing['item']['duration_ms']
    progress_ms = currently_playing['progress_ms']

    return jsonify({'artist': artist, 'song': song, 'duration_ms': duration_ms, 'progress_ms': progress_ms})


"""
PUT
"""


@app.route('/removefromlist/<string:artist><string:song>', methods=['PUT'])
def remove_from_list(artist, song):
    SpotifyTrackGrabber.playlist_delete(artist, song)


@app.route('/addtolist/<string:artist><string:song>', methods=['PUT'])
def add_to_list(artist, song):
    SpotifyTrackGrabber.playlist_add(artist, song)


"""
DELETE
"""
if __name__ == "__main__":
    app.run(debug=True)
