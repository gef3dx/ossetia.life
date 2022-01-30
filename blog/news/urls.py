from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostView.as_view(),  name='post_list'),
    path('post/<int:pk>', views.SinglePostView.as_view(),  name='post_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

