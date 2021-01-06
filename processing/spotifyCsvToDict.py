import sys
import os
import errno
import csv

spotifyDict = {}
spotifyUniqueDict = {}
flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
cur_path = os.path.dirname(__file__)
output_path = os.path.join(cur_path, "..", "data", "output1.txt")
with open(output_path, newline='') as csvfile:
    rowReader = csv.reader(csvfile)


    # extracting field names through first row

    fields = next(rowReader)
    currentRow = None
    for row in rowReader:
        # adding to dictionary indexed by date
        if row[-1] not in spotifyDict:
            spotifyDict[row[-1]] = [{"title":row[2],"artist":row[3], "streams":row[4], "id":row[5][31:]}]
        else:
            spotifyDict[row[-1]].append({"title":row[2],"artist":row[3], "streams":row[4], "id":row[5][31:]})
        # adding to dictionary indexed by (title,artist) with value id of song

        spotifyUniqueDict[(row[2],row[3])] = row[5][31:]



song_dict_path = os.path.join(cur_path, "..", "data", "song_dict_spotify.py")
with open(song_dict_path, 'w') as outfile:
    outfile.write(f"spotifyDictionary = {str(spotifyDict)}")

unique_songs_path = os.path.join(cur_path, "..", "data", "unique_songs.py")
with open(unique_songs_path, 'w') as outfile:
    outfile.write(f"spotifyUniqueDictionary = {str(spotifyUniqueDict)}")