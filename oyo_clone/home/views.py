from django.shortcuts import render

# Create your views here.



from accounts.models import Hotel


def index(request):
    hotels = Hotel.objects.all()
    if request.GET.get('search'):
        hotels = hotels.filter(hotel_name__icontains = request.GET.get('search'))

    if request.GET.get('sort_by'):
        sort_by = request.GET.get('sort_by')
        if sort_by == "sort_low":
            hotels = hotels.order_by('hotel_offer_price')
        elif sort_by == "sort_high":
            hotels = hotels.order_by('-hotel_offer_price')
    return render(request, 'index.html', context = {'hotels' : hotels[:50]})


#home/views.py
#other views
def hotel_details(request, slug):
    hotel = Hotel.objects.get(hotel_slug = slug)
    return render(request, 'hotel_detail.html', context = {'hotel' : hotel})