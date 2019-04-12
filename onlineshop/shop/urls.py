from django.urls import path
from . import views

app_name ="shop"


urlpatterns = [

    path("",views.product_list,name ="product_list"),
    path('<str:category_slug>',views.product_list, name = "product_list_by_category"),
    path('<int:id>/<str:slug>/',views.product_detail,name="product_detail"),
    path('shop/contact/',views.contact,name ="contact"),
    path('shop/about/',views.about_us,name ="about")
   
]
