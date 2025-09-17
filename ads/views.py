from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Ad

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


    

