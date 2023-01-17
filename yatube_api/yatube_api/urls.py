from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from api.views import FollowList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    # path('/api/v1/follow/', FollowList.as_view()),
]
