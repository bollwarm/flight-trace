import urllib.request
import json
import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM

fig, ax = plt.subplots()
ax=plt.axes(projection=ccrs.PlateCarree())
ax.set_ylim(40.069212,40.292426)
ax.set_xlim(116.4541,116.8334)
osm_tiles=OSM()
ax.add_image(osm_tiles,13)
ax.text(116.5946,40.0763,'Beijing CIA',horizontalalignment='right',size='large')
ax.plot([116.5946],[40.0763],'bo')

track, = ax.plot([], [],'ro')

sop = urllib.request.build_opener()
sop.addheaders = [('User-agent', 'Mozilla/5.0')]

def flash(self):
   
    fp=sop.open('http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=40.0952&lng=116.63349&fDstL=0&fDstU=20')
    ccbyte=fp.read()
    jsdata=ccbyte.decode("utf8")
    cisinfo=json.loads(jsdata)
    fp.close()
    fp.close()
    lat_list=[]
    long_list=[]
    op_list=[]
    anotation_list=[]
    
    for num,flight_data in enumerate(cisinfo['acList']):
        lat=flight_data['Lat']
        lon=flight_data['Long']
        lat_list.append(lat)
        long_list.append(lon)
        op_list.append(flight_data['Call'])

    track.set_data(long_list,lat_list)

    for num, annot in enumerate(anotation_list):
        annot.remove()
    anotation_list[:]=[]
    
    for num,annot in enumerate(js_str['acList']):
        annotation=ax.annotate('text',xy=(0,0),size='smaller')
        anotation_list.append(annotation)

    for num,ano in enumerate(anotation_list):
        ano.set_position((long_list[num],lat_list[num]))
        ano.xy = (long_list[num],lat_list[num])
        txt_op=str(op_list[num])
        ano.set_text(txt_op)

    return track,ano,

anim = animation.FuncAnimation(fig, flash,interval=5000, blit=False)

plt.show()

