import json
import re

"""
List of playlist which will include a dictionary with artists and their respective songs.
"""
playlist = []

"""
Song class which has the CRUD functionalities retrieve songs and artists and update to playlist.
"""


class Song:
    """
    GET method to grab the playlist and serialize it to json.
    """

    def GET(self):
        if len(playlist) == 0:
            return "Playlist not found."
        else:
            return json.dumps(playlist, indent=3)

    """
    PUT method to update the playlist with the selected artist and song.
    """

    def PUT(self, song=None):
        artist = ""
        songtitle = ""

        if song is None:
            return "Artist and/or song not found."
        if "-" in song:
            artist_and_songtitle = re.split(r'-', song)
            artist = artist_and_songtitle[0]
            songtitle = artist_and_songtitle[1]

        playlist.append({songtitle: artist})