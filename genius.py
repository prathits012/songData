#!/usr/bin/env python3
from songs_dict import songDictionary
import json
import lyricsgenius as lg
from os import remove
import requests

'''
Currently need to 'pip install lyricsgenius' to run this
'''

base_url = "http://api.genius.com"

# print(type(songDictionary))
print(len(songDictionary.keys()))
# print(list(songDictionary.keys()))
# exit()

with open('genius_client.json') as genius_client_info:
  client_info = json.load(genius_client_info)

client_id = client_info["client_id"]
client_secret = client_info["client_secret"]
client_access_token = client_info["client_access_token"]

genius = lg.Genius(client_access_token, skip_non_songs = True, excluded_terms = ["(Remix)", "(Live)", "(Radio Edit)"], remove_section_headers = True)

song_list = list(songDictionary.keys())

def get_lyrics (song_info_list): #should be in the form of (Song Name, Artist)
    with open("test_lyrics.txt", 'w') as outfile:
        for song_info in song_info_list:
            try:
                song = genius.search_song(song_info[0], song_info[1])
                if song.title.lower() != song_info[0].lower() and song.artist.lower() != song_info[1].lower():
                    print(f"Couldnt Find Correct Lyrics For {song_info[0]} by {song_info[1]}, Only Found {song.title} by {song.artist}")
                    continue
                outfile.write(f"\n\n\n{song.lyrics}")
                print(f"Grabbed The Lyrics From {song_info[0]} by {song_info[1]} with song_title: {song.title}")
            except:
                print(f"Error Looking Up {song_info[0]} by {song_info[1]}")

get_lyrics(song_list[:5])