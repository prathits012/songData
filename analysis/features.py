#!/usr/bin/env python3
import json
import math
import os
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

print(len(id_list))

for i in range(math.ceil(len(id_list)/100)):
    id_section_list.append(id_list[i*100:min((i+1)*100, len(id_list))])
    # print(len(id_section_list[i]))
    # print(min((i+1)*100, len(id_list)))

features_dict = {}

for section in id_section_list:
    query = {
        "ids": section
    }
    spotify = SpotifyAPI(client_id, client_secret)
    features_result = spotify.get_tracklist_features(section)
    # print(type(features_result))
    # print(type(features_result["audio_features"]))
    print(len(features_result["audio_features"]))
    song_features_dict = dict(zip(section, features_result["audio_features"]))
    # print(song_features_dict)
    # print(type(song_features_dict))
    # print()
    # exit()
    features_dict = {**features_dict, **song_features_dict}

features_path = os.path.join(cur_path, "..", "data", "features_dict.py")
with open(features_path, 'w') as outfile:
    outfile.write(f"features_dict = {str(features_dict)}")