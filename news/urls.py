from django.urls import path	
from .views import *

urlpatterns = [
	path('news/', News, name="news"),
	path(' addinfo/', addInformation, name="addinfo"),
	path('news/<str:hashid>/', blog_detail, name="blog_detail"),

	path('newsadmin/', NewsAdmin, name="newsadmin"),
	path('updateinfo/<str:hashid>/', updateInformasaun, name="updateinfo"),
    path('news/delete/<str:hashid>/', DeleteInformasaun, name="deleteinfo"),
	
]