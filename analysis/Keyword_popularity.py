#!/usr/bin/env python3
import sys
sys.path.append(".")
from processing.genius import *
# sys.path.append("../data")
from data.lyrics_dict import lyrics_dict
import json
import math
import os


def find_word_score():
    f = os.path.join(cur_path, "..", "data", "outputDaily.txt")
    f = open(f, 'r')
    f.readline()
    word_popularity = {}
    track_position = {}
    for line in f:
        position, track, artist = line.split(",")[1:3]
        track_position[(track, artist)] = position
    for track, word_dict in lyrics_dict.items():
        for word, frequency in word_dict.items():
            if word not in word_popularity:
                word_popularity[word] = 0
            word_popularity[word] += frequency/track_position[track]
    word_popularity = {"labels" : word_popularity.keys(), "data" : word_popularity.values()}

    f = os.path.join(cur_path, "..", "data", "outputWord_popularity.json")
    f = open(f, 'w')
    f.write(json.dumps(word_popularity))

        

        