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
            spotifyDict[row[-1]] = [{"title":row[2],"artist":row[3]}]
        else:
            spotifyDict[row[-1]].append([{"title":row[2],"artist":row[3]}])
        
        filename = "song_dict_spotify.py"


    # writing to file if file doesn't exist
try:
    file_handle = os.open(filename, flags)
except OSError as e:
    if e.errno == errno.EEXIST:  # Failed as the file already exists.
        print("File already Exists")
        pass
    else:  # Something unexpected went wrong so reraise the exception.
        raise
else:  # No exception, so the file must have been created successfully.
    with os.fdopen(file_handle, 'w') as file_obj:
    # Using `os.fdopen` converts the handle to an object that acts like a
    # regular Python file object, and the `with` context manager means the
    # file will be automatically closed when we're done with it.
        file_obj.write("spotifyDictionary = ")
        
        file_obj.write(str(spotifyDict))
    
    
    