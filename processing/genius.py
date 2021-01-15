#!/usr/bin/env python3
from json import decoder
from bs4 import BeautifulSoup
import sys
sys.path.append(".")
from data.songs_dict import songDictionary
from data.unique_songs import spotifyUniqueDictionary
import json
import lyricsgenius as lg
# import mechanicalSoup
import os
import string
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

song_url_list = []

table = str.maketrans(dict.fromkeys(string.punctuation))

cur_path = os.path.dirname(__file__)

def get_lyrics(song_info_list): #should be in the form of (Song Name, Artist)
    lyrics_path = os.path.join(cur_path, "..", "data", "test_lyrics.txt")
    with open(lyrics_path, 'w') as outfile:
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
    genres_path = os.path.join(cur_path, "..", "data", "test_genres.txt")
    with open(genres_path, 'w') as outfile:
        print(song_url_list)
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

            # print(alt_genres)

            primary_string = str(soup.find("script", type="text/javascript", string=re.compile("songs,tag")))
            primary_string_index = primary_string.find("songs,tag:") # length of string is 10

            counter = 0 # end calculation will be str[primary_string_index+10:primary_string_index+counter+9]
            if primary_string_index != 1:
                while primary_string[counter+primary_string_index+9] != "'":
                    counter += 1
            else:
                print("NO GENRE DETECTED")
                print(song_url)
                raise ValueError('One Song has No Genre.')
                return

            primary_genre = primary_string[primary_string_index+10:primary_string_index+counter+9]
            if "tag:" in primary_genre:
                primary_genre = primary_genre.replace("tag:", "").split(',')
                for i in range(len(primary_genre)):
                    primary_genre[i] = primary_genre[i].strip('+').replace('+', '-')

            # print(primary_genre)
            outfile.write(f"{','.join(primary_genre)}|{','.join(alt_genres)}")
            return

def make_lyrics_dict(song_info_list):
    lyrics_dict = {}
    stop_words = {}
    stopwords_path = os.path.join(cur_path, "..", "data", "stopwords.txt")
    with open(stopwords_path) as infile:
        for line in infile:
            stop_words[line.strip('\n')] = 1
    lyrics_path = os.path.join(cur_path, "..", "data", "lyrics_dict.py")
    with open(lyrics_path, 'w') as outfile:
        for song_info in song_info_list:
            try:
                song = genius.search_song(song_info[0], song_info[1])
                if song.title.lower() != song_info[0].lower() and song.artist.lower() != song_info[1].lower():
                    print(f"Couldnt Find Correct Lyrics For {song_info[0]} by {song_info[1]}, Only Found {song.title} by {song.artist}")
                    continue
                lyrics = list(song.lyrics.split())
                word_dict = {}
                for word in lyrics:
                    simple_word = word.lower()
                    simple_word = simple_word.translate(table)
                    if simple_word in stop_words or word in stop_words:
                        continue
                    if simple_word in word_dict:
                        word_dict[simple_word] += 1
                    else:
                        word_dict[simple_word] = 1
                lyrics_dict[song_info] = word_dict
                song_url_list.append(song.url)
                outfile.write(f"lyrics_dict = {str(lyrics_dict)}")
                print(f"Grabbed The Lyrics From {song_info[0]} by {song_info[1]} with song_title: {song.title}|||{song.url}")
            except:
                print(f"Error Looking Up {song_info[0]} by {song_info[1]}")

# get_lyrics(song_list[2:3])
make_lyrics_dict(song_list[2:3])
get_genre(song_url_list)
