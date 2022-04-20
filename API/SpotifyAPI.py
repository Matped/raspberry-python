import spotipy
from spotipy import SpotifyOAuth
from SpotifyUserCredentials import client_id_private, client_secret_private, redirect_uri_private, scope_private

"""
Class that grabs user credentials and has functions for finding tracks and adding them to the playlist
"""

playlist = [{'artist': 'ArtistTest', 'song': 'SongTest'}, {'artist': 'ArtistTestTwo', 'song': 'SongTestTwo'}]


class SpotifyTrackGrabber:
    spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id_private,
        client_secret=client_secret_private,
        redirect_uri=redirect_uri_private,
        scope=scope_private))

    @staticmethod
    def playlist_delete(artist, song):
        playlist.remove({'artist': artist, 'song': song})

    @staticmethod
    def playlist_add(artist, song):
        playlist.append({'artist': artist, 'song': song})

    @staticmethod
    def search_for_track(input_track):
        track = SpotifyTrackGrabber.spotify_client.search(q=input_track, limit=10, offset=0, type="track",
                                                          market=None)
        return track

    @staticmethod
    def set_track_in_queue(track_id):
        SpotifyTrackGrabber.spotify_client.add_to_queue(uri=track_id, device_id=None)

    @staticmethod
    def currently_playing():
        current_song = SpotifyTrackGrabber.spotify_client.currently_playing(market=None, additional_types="track")
        return current_song
