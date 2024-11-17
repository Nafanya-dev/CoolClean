from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from CoolClean.washers import views


urlpatterns = [
    path('', views.WasherListView.as_view(),
         name='washer-list-page'),

    path('create/', views.WasherCreateView.as_view(),
         name='create-washer-page'),

    path('<int:pk>/update/', views.WasherUpdateView.as_view(),
         name='update-washer-page'),

    path('<int:pk>/delete/', views.WasherDeleteView.as_view(),
         name='delete-washer-page'),

    path('<int:pk>/', views.WasherDetailView.as_view(),
         name='detail-washer-page'),

    path('delete-image/<int:image_id>/', views.delete_image,
         name='delete-image'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
