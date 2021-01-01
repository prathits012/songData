import sys
import os
import errno
import csv
from datetime import datetime, timedelta


import spotifyDictionary from song_dict_spotify

#charts are off by one date
yesterday = datetime.now() - timedelta(1)
date = datetime.strftime(yesterday, '%Y-%m-%d')
print(date)
flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
with open('outputDaily.txt', newline='') as csvfile:
    rowReader = csv.reader(csvfile)

      
    # extracting field names through first row 
    
    fields = next(rowReader)
    currentRow = None
    for row in rowReader:
        #print(row[-1])

        if date not in spotifyDictionary:
            # adding a new date to the dictionary
            spotifyDictionary[date] = [{"title":row[2],"artist":row[3], "streams":row[4], "id":row[5][31:]}]
        else:
            spotifyDictionary[row[-1]].append({"title":row[2],"artist":row[3], "streams":row[4], "id":row[5][31:]})
        
        filename = "song_dict_spotify_updated.py"

    

    # to delete old contents
    open(filename, 'w').close()



    # need to overwrite to file to update it
    with open(filename, 'w') as outfile:
        outfile.write(f"spotifyDictionary = {str(spotifyDict)}")
    
    
    