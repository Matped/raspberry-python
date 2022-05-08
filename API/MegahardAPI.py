import socket
from flask import *
from SpotifyAPI import *

# getting ip address of device via socket.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipaddress = s.getsockname()[0]

# variables for data.
customerAmount = 10
userAmount = 5
percentageDifference = userAmount / customerAmount * 100

app = Flask(__name__)

"""
POST
"""


@app.route('/queuesong/<string:song_id>', methods=["POST"])
def queue_song(song_id):
    SpotifyTrackGrabber.set_track_in_queue(song_id)
    return jsonify(song_id)


@app.route('/removefromlist/<string:artist><string:song>', methods=['POST'])
def remove_from_list(artist, song):
    SpotifyTrackGrabber.playlist_delete(artist, song)
    return jsonify(playlist)


@app.route('/addtolist/<string:artist>/<string:song>', methods=['POST'])
def add_to_list(artist, song):
    SpotifyTrackGrabber.playlist_add(artist, song)
    return jsonify(playlist)


"""
GET
"""


@app.route('/getuseramount', methods=['GET'])
def get_user_amount():
    return jsonify(userAmount)


@app.route('/getcustomeramount')
def get_customer_amount():
    return jsonify(customerAmount)


@app.route('/getpercentage')
def get_percentage():
    return jsonify(percentageDifference)


@app.route('/getdeviceip', methods=['GET'])
def get_device_ip():
    return jsonify(ipaddress)


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


@app.route('/useramount/<int:users>', methods=['PUT'])
def user_amount_app(users):
    global userAmount
    userAmount = users


"""
DELETE
"""
if __name__ == "__main__":
    app.run(debug=True)
