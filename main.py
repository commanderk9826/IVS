import json
import requests

url="https://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes"

r=requests.get(url)
# r=requests.get(url).text : json
# r=requests.get(url).json() : 딕셔너리

print(r.text)




