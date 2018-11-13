from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('emsaiu.urls')),
    url(r'^saml/', include('uw_saml.urls')),
]
