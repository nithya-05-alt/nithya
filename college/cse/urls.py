from django.urls import path
from cse.views import cseapp,dataView,adddata,updateData,deleteData
from django.conf.urls import include
urlpatterns = [
    path('cs/',cseapp),
    path('hey/',dataView),
    path('',adddata),
    path('upda/<int:id>',updateData),
    path('dele/<int:id>',deleteData),
    path('accounts/',include('django.contrib.auth.urls')),
]

