from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Ad
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import AdSerializer

def ads_all(request):
    ads = Ad.objects.all()
    data = list(ads.values("id", "title", "price", "city__name", "category__name"))
    return JsonResponse(data, safe=False)

def ads_by_city(request, city_name):
    ads = Ad.objects.filter(city__name__iexact=city_name)
    data = list(ads.values("id", "title", "price", "city__name", "category__name"))
    return JsonResponse(data, safe=False)

def ads_by_category(request, cat_name):
    ads = Ad.objects.filter(category__name__iexact=cat_name)
    data = list(ads.values("id", "title", "price", "city__name", "category__name"))
    return JsonResponse(data, safe=False)

@require_POST
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    ad.delete()
    return JsonResponse({"status": "ok", "deleted_id": pk})

class AllAdList(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    
class Create_ads(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    
class delete_ads(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    
class update_ads(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer





    

