
import urllib.request
import json
from pprint import pprint

def urlopen(*args, **kargs):
    pprint(json.loads(urllib.request.urlopen(*args, **kargs).read().decode('utf-8')))
