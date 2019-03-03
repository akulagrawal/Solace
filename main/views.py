from django.shortcuts import render
from main.score import ret_lat_lng, cal_score
# Create your views here.
def index_view(request):
    return render(request,'main/search_box.html')

def search_view(request):
    return render(request,'main/enter_city.html')

def results_view(request):
    print(request.GET)
    city_name = request.GET.get('city')
    city_coord = ret_lat_lng(city_name)
    all_coord = [dict() for x in range(5)]
    lat = city_coord['lat']
    lng = city_coord['lng']

    all_coord[0] = {'lat': lat, 'lng': lng}
    all_coord[1] = {'lat': lat+0.25, 'lng': lng}
    all_coord[2] = {'lat': lat-0.25, 'lng': lng}
    all_coord[3] = {'lat': lat, 'lng': lng+0.25}
    all_coord[4] = {'lat': lat, 'lng': lng-0.25}

    all_score = [dict() for x in range(5)]

    print(all_coord)
    for i in range(0,5):
    	all_score[i] = ((cal_score(all_coord[i]['lat'],all_coord[i]['lng'])))

    print(all_score)
    #all_score = [[{'latitude': 28.4743879, 'longitude': 77.50399039999999, 'score': 83.88966801235443}, {'place': 'airport', 'distance': 1.2890693626629919}, {'place': 'bus_station', 'distance': 0.18513903689995623}, {'place': 'doctor', 'distance': 0.12500065116394046}, {'place': 'fire_station', 'distance': 1.04567038344527}, {'place': 'hospital', 'distance': 6.084947487823825e-06}, {'place': 'park', 'distance': 6.084947487823825e-06}, {'place': 'police', 'distance': 0.2674067322899838}, {'place': 'taxi_stand', 'distance': 0.6513996908152861}, {'place': 'train_station', 'distance': 4.306328929750421}, {'place': 'transit_station', 'distance': 0.18513903689995623}], [{'latitude': 28.7243879, 'longitude': 77.50399039999999, 'score': 60.21813586325656}, {'place': 'airport', 'distance': 3.035282065339869}, {'place': 'bus_station', 'distance': 2.3155717422257744}, {'place': 'doctor', 'distance': 1.5670647486674816}, {'place': 'fire_station', 'distance': 3.035282065339869}, {'place': 'hospital', 'distance': 0.6296282361155335}, {'place': 'park', 'distance': 1.513550998412591}, {'place': 'police', 'distance': 2.2874140527174016}, {'place': 'taxi_stand', 'distance': 2.4740752860184703}, {'place': 'train_station', 'distance': 1.5165314367673621}, {'place': 'transit_station', 'distance': 1.5165314367673621}], [{'latitude': 28.2243879, 'longitude': 77.50399039999999, 'score': 42.207345489314015}, {'place': 'airport', 'distance': 3.0496078521550616}, {'place': 'bus_station', 'distance': 3.8285212668943096}, {'place': 'doctor', 'distance': 0.956496966455591}, {'place': 'fire_station', 'distance': 3.0496078521550616}, {'place': 'hospital', 'distance': 0.8803436755391496}, {'place': 'park', 'distance': 3.6239950891987305}, {'place': 'police', 'distance': 3.5800175817406528}, {'place': 'taxi_stand', 'distance': 3.0496078521550616}, {'place': 'train_station', 'distance': 3.0496078521550616}, {'place': 'transit_station', 'distance': 3.8285212668943096}], [{'latitude': 28.4743879, 'longitude': 77.75399039999999, 'score': 46.242253192752464}, {'place': 'airport', 'distance': 3.0424739025936214}, {'place': 'bus_station', 'distance': 1.0825674562404968}, {'place': 'doctor', 'distance': 1.350909187237476}, {'place': 'fire_station', 'distance': 3.0424739025936214}, {'place': 'hospital', 'distance': 2.714543059908867}, {'place': 'park', 'distance': 3.338750183756892}, {'place': 'police', 'distance': 3.6889185890890035}, {'place': 'taxi_stand', 'distance': 3.824266459932563}, {'place': 'train_station', 'distance': 3.711403206030731}, {'place': 'transit_station', 'distance': 1.0825674562404968}], [{'latitude': 28.4743879, 'longitude': 77.25399039999999, 'score': 63.05733199577948}, {'place': 'airport', 'distance': 1.4328628463073003}, {'place': 'bus_station', 'distance': 2.018919916809814}, {'place': 'doctor', 'distance': 0.9548024820668783}, {'place': 'fire_station', 'distance': 2.355558668220776}, {'place': 'hospital', 'distance': 1.0030975764220542}, {'place': 'park', 'distance': 0.9772650991141458}, {'place': 'police', 'distance': 1.8953212783636053}, {'place': 'taxi_stand', 'distance': 2.5115332643054917}, {'place': 'train_station', 'distance': 3.3030529536903823}, {'place': 'transit_station', 'distance': 2.018919916809814}]]

    return render(request,'main/result.html',{'score_data':all_score})