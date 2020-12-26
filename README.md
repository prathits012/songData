songData
============

This a project to analyze trends in popular songs using the billboard.py github repo 
[![Build Status](https://travis-ci.org/guoguo12/billboard-charts.svg)](https://travis-ci.org/guoguo12/billboard-charts)

**billboard.py** is a Python API for accessing music charts from [Billboard.com](http://www.billboard.com/charts/).

Installation for billboard.py
------------

Required for proper functioning

clone this repo and run `python setup.py install`.



Year-end charts have `previousYear` (and `nextYear`) instead.


### More resources

For additional documentation, look at the file `billboard.py`, or use Python's interactive `help` feature.

Think you found a bug? Create an issue [here](https://github.com/guoguo12/billboard-charts/issues).



### Running tests

to be updated

```
nosetests
```

To run the test suite locally on both Python 2.7 and 3.4, install [tox](https://tox.readthedocs.org/en/latest/) and run

```
tox
```



Dependencies
------------
* [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://requests.readthedocs.org/en/latest/)

License
-------

* This project is licensed under the MIT License.
* The *Billboard* charts are owned by Prometheus Global Media LLC. See Billboard.com's [Terms of Use](http://www.billboard.com/terms-of-use) for more information.
