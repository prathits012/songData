#!/usr/bin/env python3
#from file import dict
import json
import lyricsgenius as lg
from os import remove
import requests

base_url = "http://api.genius.com"

file = open("test_lyrics.txt", 'w')

with open('genius_client.json') as genius_client_info:
  client_info = json.load(genius_client_info)

client_id = client_info["client_id"]
client_secret = client_info["client_secret"]
client_access_token = client_info["client_access_token"]

genius = lg.Genius(client_access_token, skip_non_songs = True, excluded_terms = ["(Remix)", "(Live)", "(Radio Edit)"], remove_section_headers = True)

test_list = [("The Box", "Roddy Ricch"), ("Drown", "Clairo")]

def get_lyrics (song_info_list): #should be in the form of (Song Name, Artist)
    for song_info in song_info_list:
        try:
            song = genius.search_song(song_info[0], song_info[1])
            if song.title != song_info[0] and song.artist != song_info[1]:
                print(f"Couldnt Find Correct Lyrics For {song_info[0]} by {song_info[1]}, Only Found {song.title} by {song.artist}")
                continue
            file.write(f"\n\n{song.lyrics}")
            print(f"Grabbed The Lyrics From {song_info[0]} by {song_info[1]} with song_title: {song.title}")
        except:
            print(f"Error Looking Up {song_info[0]} by {song_info[1]}")

get_lyrics(test_list)