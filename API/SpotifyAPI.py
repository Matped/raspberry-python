import spotipy
import requests
from spotipy import SpotifyOAuth
from SpotifyUserCredentials import client_id_private, client_secret_private, redirect_uri_private, scope_private

"""
Class that grabs user credentials and has functions for finding tracks and adding them to the playlist
"""

playlist = []


class SpotifyTrackGrabber:
    spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id_private,
        client_secret=client_secret_private,
        redirect_uri=redirect_uri_private,
        scope=scope_private))

    def playlist_delete(self, artist, song):
        playlist.remove({'artist': artist, 'song': song})

    def playlist_add(self, artist, song):
        playlist.append({'artist': artist, 'song': song})

    def search_for_track(self, input_track):
        track = SpotifyTrackGrabber.spotify_client.search(q=input_track, limit=10, offset=0, type="track",
                                                          market=None)
        return track

    def set_track_in_queue(self, track_id):
        SpotifyTrackGrabber.spotify_client.add_to_queue(uri=track_id, device_id=None)

    def currently_playing(self):
        current_song = SpotifyTrackGrabber.spotify_client.currently_playing(market=None, additional_types="track")
        return current_song
