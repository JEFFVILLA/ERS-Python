import json
import urllib
from urllib.request import urlopen


response = urlopen('http://vimeo.com/api/v2/video/85517984.json')
data = json.load(response)
