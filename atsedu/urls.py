"""atsedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include, url
from ats import views as core_views
from django.contrib.auth import views as auth_views
# from ats import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', core_views.index, name='index'),
    # url(r'$',core_views.index,name="index"),
    # url(r'^about/$',core_views.about,name="about"),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^login/$','django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^$', core_views.index, name='index'),
    url(r'^about/$',core_views.about,name="about"),
    # url(r'^contact/$',core_views.contact,name="contact"),
    url(r'^email/$', core_views.email, name='email'),
    url(r'^success/$', core_views.success, name='success'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,  {'template_name': 'password_reset_done.html'},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,  {'template_name': 'password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,  {'template_name': 'password_reset_complete.html'},name='password_reset_complete'),
   
]
