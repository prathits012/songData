#!/usr/bin/python3
from datetime import datetime, timedelta
import os


yesterday = datetime.now() - timedelta(1)
yesterday = datetime.strftime(yesterday, '%Y-%m-%d')

a_year_ago = datetime.now() - timedelta(365)
a_year_ago = datetime.strftime(a_year_ago, '%Y-%m-%d')

os.system(f"python3 processing/charts.py --START-DATE {a_year_ago} --END-DATE {yesterday}")

os.system("python3 processing/spotifyCsvToDict.py")

os.system("python3 processing/genius.py")

os.system("python3 analysis/features.py")

os.system("python3 analysis/Keyword_popularity.py")