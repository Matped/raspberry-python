import spotipy
import numpy
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

    def add_tracks_to_playlist(self, input_track):
        selected_track = input_track
        track = SpotifyTrackGrabber.spotify_client.search(q=selected_track, limit=10, offset=0, type="track",
                                                          market=None)
        song_url = track['tracks']['items'][0]['album']['external_urls']['spotify']
