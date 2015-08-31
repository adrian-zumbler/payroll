"""ideal_payroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
	url(r'^agents/', include('agents.urls',namespace="agents")),
	url(r'^occupancy/', include('occupancy.urls',namespace="occupancy")),
    url(r'^auxiliarReport/', include('auxiliar_report.urls',namespace="auxiliar_report")),
    url(r'^scheduleReport/', include('schedule_report.urls',namespace="shedule_report")),
    url(r'^payroll/', include('payroll.urls',namespace="payroll")),
    url(r'^profile/', include('profiles.urls',namespace="profiles")),
    url(r'^import/',include('import_files.urls',namespace="import_files")),
    url(r'^validate/',include('validate_payroll.urls',namespace="validate_payroll")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
