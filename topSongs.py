import billboard
import pprint

def getSongs(pastYears = 10, chartTitle = 'hot-100-songs', yearStart = 2019):
    # looping through ChartData objects to store the data in a large dictionary
    # storing song title, artist, ranking, and year 
    # currently year end charts are only supported from 2015
    print(yearStart)
    songDict = {}
    # structure of songDict
    # Key  is struct of title and artists accesible by dot notation
    # Value is tuple of (year, rank)
    for year in range(yearStart,yearStart-pastYears,-1):
        #print(year)

    
        
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
    #print(len(songDict))
    pp = pprint.PrettyPrinter(indent=4, compact=True)
    pp.pprint(songDict)
    return songDict
if __name__ == "__main__":
    getSongs(3)