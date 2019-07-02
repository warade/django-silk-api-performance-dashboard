# How to use django-silk for API debugging.
1. Create a virtual environment.
```
vartualenv .
source bin/activate
```
2. Install
```
pip3 install django-silk
pip3 install graphitesend
pip3 install pyformance
```
graphitesend and pyformance are installed because of I used this same project for Graphite project.

3. 
```
MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',
    ...
]
```
4. 
```
INSTALLED_APPS = (
    ...
    'silk'
)
```
5. Add this url in your urlpatterns
```
url(r'^silk/', include('silk.urls', namespace='silk'))
```
6 By visiting localhost:8000/silk/ you can see a dashboard, use following curls to hit the endpoints.
```
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/users/

curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" http://127.0.0.1:8000/users/ -d '{"username": "xyz","first_name": "ddd","last_name": "fff","email": "som@gmail.com"}' | grep }| python3 -mjson.tool
```
