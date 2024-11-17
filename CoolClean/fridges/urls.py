from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from CoolClean.fridges import views


urlpatterns = [
    path('', views.FridgeListView.as_view(),
         name='fridge-list-page'),

    path('create/', views.FridgeCreateView.as_view(),
         name='create-fridge-page'),

    path('<int:pk>/update/', views.FridgeUpdateView.as_view(),
         name='update-fridge-page'),

    path('<int:pk>/delete/', views.FridgeDeleteView.as_view(),
         name='delete-fridge-page'),

    path('<int:pk>/', views.FridgeDetailView.as_view(),
         name='detail-fridge-page'),

    path('delete-image/<int:image_id>/', views.delete_image,
         name='delete-image'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
