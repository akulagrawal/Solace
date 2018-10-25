from django.shortcuts import render
from main.score import ret_lat_lng, cal_score
# Create your views here.
def index_view(request):
    return render(request,'main/search_box.html')

def search_view(request):
    return render(request,'main/enter_city.html')

def results_view(request):
    print(request.GET)
    # city_name = 'noida'
    # city_coord = ret_lat_lng(city_name)
    # all_coord = [dict() for x in range(5)]
    # lat = city_coord['lat']
    # lng = city_coord['lng']

    # all_coord[0] = {'lat': lat, 'lng': lng}
    # all_coord[1] = {'lat': lat+0.25, 'lng': lng}
    # all_coord[2] = {'lat': lat-0.25, 'lng': lng}
    # all_coord[3] = {'lat': lat, 'lng': lng+0.25}
    # all_coord[4] = {'lat': lat, 'lng': lng-0.25}

    # all_score = [dict() for x in range(5)]

    # print(all_coord)
    # for i in range(0,5):
    # 	all_score[i] = ((cal_score(all_coord[i]['lat'],all_coord[i]['lng'])))

    # print(all_score)

    return render(request,'main/result.html')