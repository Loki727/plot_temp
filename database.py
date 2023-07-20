import requests
import json

API="appid={enter API from openweathermap.org}"
LINK="http://api.openweathermap.org/data/2.5/forecast?"
CITY="q=London,us&"
UNTILS="units=metric&"
def getAPIData():
    completeLink=LINK+CITY+UNTILS+API
    response = requests.get(completeLink)
    dictResponse=json.loads(response.text)
    return dictResponse

