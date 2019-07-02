from django.conf.urls import include, url
from django.contrib import admin
from quickstart import views
from django.conf import settings
#import debug_toolbar
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
	url(r'rest-auth/', include('rest_auth.urls')),
	url(r'^silk/', include('silk.urls', namespace='silk')),
	#url(r'__debug__/', include(debug_toolbar.urls))
	#url(r'rest-auth/registration/', include('rest_auth.registration.urls')),
]

# curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/users/
# curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" http://127.0.0.1:8000/users/ -d '{"username": "xyz","first_name": "ddd","last_name": "fff","email": "som@gmail.com"}' | grep }| python -mjson.tool