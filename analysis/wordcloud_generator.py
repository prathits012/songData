#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os
import requests
import sys
sys.path.append(".")
from data.lyrics_dict import lyrics_dict
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

test_list = ["hello", "hello", "hi", "prathit", "michael"]
test_string = "hello hello hi prathit michael"
test_dict = {}
test_dict["prathit"] = 5
test_dict["gagin"] = 2
test_dict["suraj"] = 10

stopwords = set(STOPWORDS)

cur_path = os.path.dirname(__file__)
print(lyrics_dict.keys())

def create_songcloud(song_info, image_link = ""):
    album_coloring = np.array(Image.open(requests.get(image_link, stream=True).raw))
    wordcloud = WordCloud(width = 640, height = 640,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate_from_frequencies(lyrics_dict[song_info])
    image_colors = ImageColorGenerator(album_coloring)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud.recolor(color_func=image_colors))
    plt.axis("off")
    plt.tight_layout(pad = 0)
    cloud_path = os.path.join(cur_path, "..", "data", f"{song_info[0]}-cloud.jpeg")
    plt.savefig(cloud_path)

def create_all_songclouds():
    count = 0
    for key in lyrics_dict.keys():
        wordcloud = WordCloud(width = 640, height = 640,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate_from_frequencies(lyrics_dict[key])
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        cloud_path = os.path.join(cur_path, "..", "data", f"songcloud{count}.jpeg")
        plt.savefig(cloud_path)
        count += 1
        if count > 10:
            break


create_songcloud(('Without Me', 'Halsey'), image_link = "https://i.scdn.co/image/ab67616d0000b273c42acc1b86597285c2c79559")

