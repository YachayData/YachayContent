import numpy as np


from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import seaborn 

name_csv = '../output/data.csv'


df = pd.read_csv(name_csv)
