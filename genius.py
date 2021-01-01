#!/usr/bin/env python3
from json import decoder
from bs4 import BeautifulSoup
from songs_dict import songDictionary
import json
import lyricsgenius as lg
# import mechanicalSoup
from os import remove
import random
import re
import requests
from urllib.request import Request, urlopen
from urllib.parse import unquote
from user_agents import user_agent_list

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

user_agent_list

song_url_list = []

def get_lyrics(song_info_list): #should be in the form of (Song Name, Artist)
    with open("test_lyrics.txt", 'w') as outfile:
        for song_info in song_info_list:
            try:
                song = genius.search_song(song_info[0], song_info[1])
                if song.title.lower() != song_info[0].lower() and song.artist.lower() != song_info[1].lower():
                    print(f"Couldnt Find Correct Lyrics For {song_info[0]} by {song_info[1]}, Only Found {song.title} by {song.artist}")
                    continue
                outfile.write(f"\n\n\n{song.lyrics}")
                song_url_list.append(song.url)
                print(f"Grabbed The Lyrics From {song_info[0]} by {song_info[1]} with song_title: {song.title}|||{song.url}")
            except:
                print(f"Error Looking Up {song_info[0]} by {song_info[1]}")

def get_genre(song_url_list): #should scrape primary genre from the URL provided by get_lyrics
    with open("test_genres.txt", 'w') as outfile:
        for song_url in song_url_list:
            print(song_url)
            agent = random.choice(user_agent_list)
            req = Request(song_url, headers={'User-Agent': agent})
            page = urlopen(req)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")

            alt_string = soup.find("img", src=re.compile("https://loadus.exelator.com/"))['src']

            alt_string_index = alt_string.find("page-genres=")
            counter = 0
            if alt_string_index != 1:
                while alt_string[alt_string_index+counter+12:alt_string_index+counter+19] != "page-in":
                    counter += 1
            else:
                print("NO SECONDARY GENRES DETECTED")

            alt_genres = unquote(alt_string[alt_string_index+12:alt_string_index+counter+11]) #unquote decodes URL specific character substitutions
            alt_genres = alt_genres.replace("Genius", "").split(',')
            for i in range(len(alt_genres)):
                alt_genres[i] = alt_genres[i].strip('+').replace('+', '-').lower()

            print(alt_genres)

            primary_string = str(soup.find("script", type="text/javascript", string=re.compile("songs,tag")))
            primary_string_index = primary_string.find("songs,tag:") # length of string is 10

            counter = 0 # end calculation will be str[primary_string_index+10:primary_string_index+counter+9]
            if primary_string_index != 1:
                while primary_string[counter+primary_string_index+9] != "'":
                    counter += 1
            else:
                print("NO GENRE DETECTED")
                return

            primary_genre = primary_string[primary_string_index+10:primary_string_index+counter+9]
            if "tag:" in primary_genre:
                primary_genre = primary_genre.replace("tag:", "").split(',')
                for i in range(len(primary_genre)):
                    primary_genre[i] = primary_genre[i].strip('+').replace('+', '-')

            print(primary_genre)
            return


get_lyrics(song_list[2:3])
get_genre(song_url_list)
