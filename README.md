# vastu_hfc_sample

-> step one pull image
docker pull jigneshkotadiya000/vastu_hfc_sample_django_api

-> step two execute image
docker run -p 8000:8000 jigneshkotadiya000/vastu_hfc_sample_django_api

-> visit url in browser
url for api doc :- http://127.0.0.1:8000/
url for admin panel :- http://127.0.0.1:8000/admin

-> admin user credentials
user:- admin@admin.com
pass:- admin



-> docker image create

docker build -t django_project .
docker run -p 8000:8000 django_project
