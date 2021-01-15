#!/usr/bin/env python3

import json
import sys
sys.path.append(".")
from spotify_client import SpotifyAPI

with open('spotify_client.json') as spotify_client_info:
  client_info = json.load(spotify_client_info)

client_id = client_info["client_id"]
client_secret = client_info["client_secret"]

'''
Valid Query Parameters:
q (REQ): Search query keywords and optional field filters and operators.
type (REQ): A comma-separated list of item types to search across.
    Valid types are: album , artist, playlist, track, show and episode.
    Search results include hits from all the specified item types.
market (OPT): An ISO 3166-1 alpha-2 country code or the string from_token.
    If a country code is specified, only artists, albums, and tracks with
        content that is playable in that market is returned.
limit (OPT): Maximum number of results to return.
    Default: 20
    Minimum: 1
    Maximum: 50
offset (OPT): The index of the first result to return.
    Default: 0 (the first result).
    Maximum offset (including limit): 2,000.
    Use with limit to get the next page of search results.
include_external (OPT): Possible values: audio
    If include_external=audio is specified the response will include any
        relevant audio content that is hosted externally.
    By default external content is filtered out from responses.
'''

playlist_id = "37i9dQZEVXbLRQDuF5jeBp"

query = {
    "q": "A lannister always pays his debts",
    "limit": "3"
}

spotify = SpotifyAPI(client_id, client_secret)
# track_results = spotify.search(query, search_type="track")
playlist_results = spotify.get_playlist_tracks(playlist_id) # returns tracks
print(playlist_results["items"][6]["track"].keys())
# print(playlist_results["items"][6]["track"]["name"])
#   get song's name (can grab id)
# print(playlist_results["items"][6]["track"]["artists"][0]["name"])
#   get 1 artist's name (can grab id)
# print(track_results["tracks"])

track_image_list = []

def get_track_images():
    for track in playlist_results["tracks"]:
        track_image_list.append(track["images"][0]["url"])
