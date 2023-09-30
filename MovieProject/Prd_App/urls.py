from .import views
from django.urls import path

app_name='Prd_App'

urlpatterns = [
    path('',views.demo,name='demo'),
    path('movie/<int:movie_id>/',views.Parti_id,name='Parti_id'),
    path('Add/',views.Add_data,name='Add_data'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]