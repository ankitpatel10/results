
from django.urls import path
from . import views
#
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="SKHome"),
    path('cr', views.cr, name='cr'),
    path('cur', views.cur, name='cur'),
    path('search', views.search, name="search")

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)