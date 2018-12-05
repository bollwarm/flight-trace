import urllib.request
import json

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#SEND QUERY (IN THE FUNCTION)
fp=opener.open('http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=40.0952&lng=116.63349&fDstL=0&fDstU=20')
mybyte=fp.read()
mystr=mybyte.decode("utf8")
js_str=json.loads(mystr)
fp.close()

print(js_str)