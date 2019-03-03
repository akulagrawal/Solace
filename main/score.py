#!/usr/bin/env python
# coding: utf-8

# In[1]:


import googlemaps


# In[2]:


#import os
#os.environ['http_proxy'] = "http://:@:" 
#os.environ['https_proxy'] = "http://:@:"

gmaps = googlemaps.Client(key='AIzaSyD4gTlyrAaD5wN9zit_lSKLiNIGWhgKtwc')



# In[3]:

def ret_lat_lng(city_name):
    geocode_result = gmaps.geocode(city_name)
    return geocode_result[0]['geometry']['location']


def cal_score(lat, lng):


    # In[5]:
    LOCATION = {'lat': lat, 'lng': lng}


    loc = [dict() for x in range(20)]
    name = ["" for x in range(20)]
    dist = [float for x in range(20)]


    # In[6]:


    # #nearby_airport = gmaps.places_nearby(location=LOCATION, radius=None, keyword=None,
    # #                  language=None, min_price=None, max_price=None, name=None,
    # 3                  open_now=False, rank_by='distance', type='airport', page_token=None)
    # print(nearby_airport)


    # # In[7]:


    # airport_loc = nearby_airport['results'][0]['geometry']['location']
    # airport_name = nearby_airport['results'][0]['name']


    # In[8]:


    places = ['airport',
    'bus_station',
    'doctor',
    'fire_station',
    'hospital',
    'park',
    'police',
    'taxi_stand',
    'train_station',
    'transit_station']


    # In[9]:


    n = len(places)
    for i in range(0,n):
        print('...',end='')
    print('')
    for i in range(0,n):
        nearby = gmaps.places_nearby(location=LOCATION, radius=None, keyword=None,
                  language=None, min_price=None, max_price=None, name=None,
                  open_now=False, rank_by='distance', type=places[i], page_token=None)
        try:
            loc[i] = nearby['results'][0]['geometry']['location']
            name[i] = nearby['results'][0]['name']
        except:
            loc[i] = {'lng': lng+0.05, 'lat': lat}
            name[i] = ''
        print('-->',end='')


    # In[10]:


    for i in range(0,n):
        print(loc[i])
        print(name[i])
        print(places[i])
        print('')


    # In[11]:


    from geopy.distance import geodesic


    # In[12]:


    print(loc[0])
    print(LOCATION)


    # In[13]:


    for i in range(0,n):
        l1 = (LOCATION['lat'], LOCATION['lng'])
        l2 = (loc[i]['lat'], loc[i]['lng'])
        dist[i] = geodesic(l1, l2).miles


    # In[14]:


    print(dist)


    # In[15]:


    for i in range(0,n):
        print(loc[i])
        print(name[i])
        print(places[i])
        print(dist[i])
        print('')


    # In[16]:


    import json


    # In[17]:


    with open('convertcsv.json', 'r') as f:
        data = json.load(f)


    # In[18]:


    print(data)


    # In[19]:


    print(data[0])


    # In[20]:


    print(len(data))
    m = len(data)


    # In[26]:


    equake = 0
    for i in range(0,m):
        l1 = (LOCATION['lat'], LOCATION['lng'])
        l2 = (data[i]['Latitude'], data[i]['Longitude'])
        d = geodesic(l1, l2).miles
        if(d <= 50):
            equake += 1


    # In[27]:


    equake


    # In[28]:


    score = 0
    print(dist[0])
    for i in range(0,n):
        if(dist[i] < 5.0):
            score += 5 - dist[i]
    score /= 5*n
    print(score)


    # In[29]:


    score /= (equake + 1)


    # In[30]:


    score *= 100
    print(score)


    # In[40]:


    data = []
    import json
    obj = {u"latitude": lat, u"longitude": lng, u"score": score}
    data.append(obj)
    for i in range(0,n):
        obj = {u"place": places[i], u"distance": dist[i]}
        data.append(obj)
    print(json.dumps(data, indent=4))
    #print(json.dumps(list(dist)))


    # In[41]:


    #with open('score.json', 'w') as outfile:
    #    json.dump(data, outfile)

    return data

