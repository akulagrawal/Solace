from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'main/search_box.html')

def search_view(request):
    return render(request,'main/enter_city.html')

def results_view(request):
    print(request.GET)
    return render(request,'main/result.html')