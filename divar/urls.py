
from django.contrib import admin
from django.urls import path
from ads.views import ads_all , ads_by_city ,  ads_by_category , ad_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', ads_all),
    path("ads/city/<str:city_name>/", ads_by_city),
    path("ads/category/<str:cat_name>/", ads_by_category),
    path("ads/<int:pk>/delete/", ad_delete),
]
