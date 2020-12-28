#!/usr/bin/env python3
# from db import db (maybe need two for both spotify and genius)

from Levenshtein import distance as levenshtein_distance
from songs_dict import songDictionary

'''
Currently need to 'pip install python-levenshtein' to run this
'''

def distance(spotify_name, genius_name):
    lev_dist = levenshtein_distance(spotify_name, genius_name) / max(len(spotify_name), length(genius_name))
    return lev_dist

def valid_search(dist):
    if dist > .9:
        return True
    return False

# search_score = 0
# searches = 0
# for spotify_song_name, genius_song_name, in db:
#   search_score += distance(spotify_song_name, genius_song_name)
#   searched += 1
# search_score /= searches
# if valid_search(search_score):
#   print("Statistically Significant Search")
# else:
#   print("Statistically Insignificant Search")
# print(search_score)
