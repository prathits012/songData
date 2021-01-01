import sys
import os
import errno
import csv

spotifyDict = {}
flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
with open('output1.txt', newline='') as csvfile:
    rowReader = csv.reader(csvfile)


    # extracting field names through first row

    fields = next(rowReader)
    currentRow = None
    for row in rowReader:
        #print(row[-1])
        if row[-1] not in spotifyDict:
            # adding a new date to the dictionary
            spotifyDict[row[-1]] = [{"title":row[2],"artist":row[3], "streams":row[4], "id":row[5][31:]}]
        else:
            spotifyDict[row[-1]].append([{"title":row[2],"artist":row[3], "streams":row[4], "id":row[5][31:]}])

        filename = "song_dict_spotify.py"


with open(filename, 'w') as outfile:
    outfile.write(f"spotifyDictionary = {str(spotifyDict)}")
