from django.urls import path
from . import views

urlpatterns = [
    path('relatorius/', views.lista_relatoriu, name='lista_relatoriu'),
    # path('relatoriu/<int:relatoriu_id>/', views.detalhu_relatoriu, name='detalhu_relatoriu'),
    # path('relatoriu/novu/', views.kriasa_relatoriu, name='kriasa_relatoriu'),

    # ADMIN
    path('relatoriusadmin/', views.lista_relatoriuAdmin, name='lista_relatoriuAdmin'),
    # path('relatoriuadmin/<str:hashid>/', views.detalhu_relatoriuAdmin, name='detalhu_relatoriuAdmin'),
    path('relatoriuadmin/Adisiona/', views.addRelatoriu, name='addRelatoriu'),
    path('relatoriuadmin/atualiza/<str:hashid>/', views.atualiza_relatoriu, name='atualiza_relatoriu'),
    path('relatoriuadmin/hamos/<str:hashid>/', views.delete_relatoriu, name='delete_relatoriu'),
    # path('relatoriuadmin/hamos/<int:relatoriu_id>/', views.hamos_relatoriu, name='hamos_relatoriu'),  
    
]