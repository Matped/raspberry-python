import spotipy
import requests
from spotipy import SpotifyOAuth
from SpotifyUserCredentials import client_id_private, client_secret_private, redirect_uri_private, scope_private

"""
Playlist of the raspberry pi unit.
"""
playlist = []

"""
Class that grabs user credentials and has functions for finding tracks and adding them to the playlist
"""


class SpotifyTrackGrabber:
    spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id_private,
        client_secret=client_secret_private,
        redirect_uri=redirect_uri_private,
        scope=scope_private))

    def search_for_track(self, input_track):
        track = SpotifyTrackGrabber.spotify_client.search(q=input_track, limit=10, offset=0, type="track",
                                                          market=None)
        song_id = track['tracks']['items'][0]['id']
        return song_id

    def set_track_in_queue(self, track_id):
        SpotifyTrackGrabber.spotify_client.add_to_queue(uri=track_id, device_id=None)

    def get_queue(self):
        queue = SpotifyTrackGrabber.spotify_client.current_playback(market=None, additional_types="track")
        return queue


print(SpotifyTrackGrabber.get_queue(SpotifyTrackGrabber))