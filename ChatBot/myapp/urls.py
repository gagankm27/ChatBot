from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('getResponse/', views.get_response, name='get_response'),
    # path('specfic',views.specfic,name='specfic'),
    # path('article/<int:article_id>',views.article)
]
