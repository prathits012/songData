songData
============

This a project to analyze trends in the daily/weekly spotify charts and display the results on an interactive website


**processing/charts.py** is a Python script for accessing music charts from [spotifycharts](http://www.spotifycharts.com)
 
Link to [fbkarsdorp/spotify-chart](https://github.com/fbkarsdorp/spotify-chart)


**processing/genius.py** is a Python script for accessing lyrics from [genius](http://www.genius.com)

Link to [johnwmillr/LyricsGenius](https://github.com/johnwmillr/LyricsGenius)


Installation for updateScript.py
------------

updateScript.py is a wrapper that runs all of the code to update the data for today's date

In order to run you must have python3 and pip installed

After installing the requirements.txt run 

``` 
python3 updateScript.py --TODAY'S DATE (YYYY/MM/DD)
```

If you want to just run specific files, read through the script for the specific commands used

### More resources

For additional documentation, use read through the individual files or the linked repo's README's 
You may also use Python's interactive `help` feature

Think you found a bug? Create an issue.



### Running tests

to be updated



Dependencies
------------
* [beautifulsoup 4](http://www.crummy.com/software/BeautifulSoup/)
* [requests](http://requests.readthedocs.org/en/latest/)
* [pandas](https://github.com/pandas-dev/pandas)
* [lyricsgenius](https://github.com/johnwmillr/LyricsGenius)


License
-------

* This project is licensed under the MIT License.
