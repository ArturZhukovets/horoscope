from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_main, name='horoscope-index'),
    path('type/', views.info_about_type_of_sign_of_zodiac),
    path('type/<str:type_zodiac>/', views.one_of_type, name='one-of-four'),
    path('<int:mounth>/<int:day>', views.get_info_by_date),
    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
    path('<str:sign_zodiac>/for-30-days-<slug:zodiac_slug>/', views.get_horoscope_for_30_days, name='horoscope-for-30-days'),



]