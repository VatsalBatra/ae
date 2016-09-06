from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings
from questions import views as questionviews

urlpatterns = [
    url(r'^$', questionviews.front, name = 'firstpage'),
    url(r'^$', questionviews.about, name = 'about'),
    url(r'^admin/', admin.site.urls),

    url(r'^questions/', include('questions.urls')),

] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)