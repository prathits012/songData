#!/usr/bin/env python3

import json
import math
import os
from songData.analysis import spotify
import sys
sys.path.append(".")
from spotify_client import SpotifyAPI
from data.unique_songs import spotifyUniqueDictionary

with open('spotify_client.json') as spotify_client_info:
  client_info = json.load(spotify_client_info)

client_id = client_info["client_id"]
client_secret = client_info["client_secret"]

'''
Valid Query Parameters:
ids (REQ): A comma-separated list of the Spotify IDs for the tracks.
    Maximum: 100 IDs.
'''

id_list = list(spotifyUniqueDictionary.values())

id_section_list = []

cur_path = os.path.dirname(__file__)

for i in range(math.ceil(len(id_list)/100)):
    id_section_list.append(id_list[i:min((i+1)*100, len(id_list))])

for section in id_section_list:
    query = {
        "ids": section
    }
    features_path = os.path.join(cur_path, "..", "data", "features_dict.py")
    with open(features_path, 'w') as outfile:
        spotify = SpotifyAPI(client_id, client_secret)
        features_result = spotify.get_tracklist_features(section)
        print(features_result)
        exit()

