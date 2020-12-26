import sys
import os
import errno
import billboard


def getSongs(pastYears = 10, chartTitle = 'hot-100-songs', yearStart = 2019, filename = "songObj.py"):
    # looping through ChartData objects to store the data in a large dictionary
    # storing song title, artist, ranking, and year 
    # currently year end charts are only supported from 2015
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    print(yearStart)
    songDict = {}
    # structure of songDict
    # Key  is struct of title and artists accesible by dot notation
    # Value is tuple of (year, rank)
    for year in range(yearStart,yearStart-pastYears,-1):
        print(year)

    
        
        chart = billboard.ChartData(chartTitle, year=year)
        rank = 0
        # entry is a chartData object that has (title,artists)
        for entry in chart.entries:
            rank+=1
            # add to dictionary, check for duplicates from later years
            songTuple = (entry.title,entry.artist)
            if songTuple in songDict:
                if songDict[songTuple][1] > rank:
                    # updating rank and year if song was ranked higher
                    
                    songDict[songTuple] = (year,rank)
            else:
                songDict[songTuple] = (year,rank)


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
            file_obj.write("songDictionary = ")
            
            file_obj.write(str(songDict))
    
    
    return songDict


# running as script
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv)==1:
        print('python3 test.py <outputFile> <yearStart> <numPastYears> <chart-title> \nNote: outputFile is required, only year-end charts are supported')
        print("Year End Chart Names: ")
        print(billboard.charts(year_end=True))
        sys.exit(1)
    if len(sys.argv)==2:
        getSongs(filename = sys.argv[1])
    if len(sys.argv)==3:
        getSongs(filename = sys.argv[1],yearStart=int(sys.argv[2]))
    if len(sys.argv)==4:
        getSongs(filename = sys.argv[1],yearStart=int(sys.argv[2]),pastYears=int(sys.argv[3]))
    if len(sys.argv)==5:
        getSongs(filename = sys.argv[1],yearStart=int(sys.argv[2]),pastYears=int(sys.argv[3]),chartTitle=sys.argv[4])

