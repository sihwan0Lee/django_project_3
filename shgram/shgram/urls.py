"""shgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

from contents.views import HomeView, RelationView


class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


# name에 설정 된부분이 html과 연결된다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
    path('', HomeView.as_view(), name='home'),
    path('login/', NonUserTemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', NonUserTemplateView.as_view(template_name='register.html'),
         name='register'),
    path('relation/', RelationView.as_view(), name='relation'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
# 미디어 세팅
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
