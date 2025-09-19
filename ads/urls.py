
from django.urls import path
from ads.views import ads_all , ads_by_city ,  ads_by_category , ad_delete, AllAdList , Create_ads , delete_ads , update_ads


urlpatterns = [
    path('', ads_all),
    path("city/<str:city_name>/", ads_by_city),
    path("category/<str:cat_name>/", ads_by_category),
    path("<int:pk>/delete/", ad_delete),
    path("ads-list-rest",  AllAdList.as_view()),
    path("create-ads",  Create_ads.as_view()),
    path("delete-ads/<str:pk>",  delete_ads.as_view()),
    path("update-ads/<str:pk>",  update_ads.as_view()),
]
