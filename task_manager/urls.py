from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

import users.views

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('users/', include('users.urls')),
    path('login/', users.views.user_login, name='login'),
    path('logout/', users.views.user_logout, name='logout'),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
)
