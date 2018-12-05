import urllib.request
import json

sop = urllib.request.build_opener()
sop.addheaders = [('User-agent', 'Mozilla/5.0')]

fp=sop.open('http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=40.0952&lng=116.63349&fDstL=0&fDstU=20')
ccbyte=fp.read()
jsdata=ccbyte.decode("utf8")
cisinfo=json.loads(jsdata)
fp.close()

print(cisinfo)

