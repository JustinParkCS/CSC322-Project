"""cuisino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

from users import views as users_views
# from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('restaurant.urls')),
    # path('register/', users_views.register),
    # path('', home_views.landing_page),

    url(r'^$',users_views.home,name='home'),
    url(r'^users/',include('users.urls')),
    url(r'^restaurant/',include('restaurant.urls')),
    url(r'^logout/$', users_views.user_logout, name='logout'),
    url(r'^special/',users_views.special,name='special'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
