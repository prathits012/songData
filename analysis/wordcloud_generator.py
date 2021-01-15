#!/usr/bin/env python3
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(".")
from data.lyrics_dict import lyric_dict
from wordcloud import WordCloud, STOPWORDS

test_list = ["hello", "hello", "hi", "prathit", "michael"]
test_string = "hello hello hi prathit michael"
test_dict = {}
test_dict["prathit"] = 5
test_dict["gagin"] = 2
test_dict["suraj"] = 10

stopwords = set(STOPWORDS)

cur_path = os.path.dirname(__file__)
count = 0
print(lyric_dict.keys())
for key in lyric_dict.keys():
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate_from_frequencies(lyric_dict[key])
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    cloud_path = os.path.join(cur_path, "..", "data", f"songcloud{count}.png")
    plt.savefig(cloud_path)
    count += 1
    if count > 10:
        break


