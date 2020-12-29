import csv

spotifyDict = {}
with open('output1.txt', newline='') as csvfile:
    rowReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    currentRow = None
    for row in rowReader:
        print(row[-1])
        if row[-1] not in spotifyDict:
            # adding a new date to the dictionary
            spotifyDict[row[-1]] = [{"title":row[2],"artist":row[3]}]
