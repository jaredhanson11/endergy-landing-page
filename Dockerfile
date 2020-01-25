FROM nginx
COPY ./index.html /usr/share/nginx/html
COPY ./css /usr/share/nginx/html/css
COPY ./js /usr/share/nginx/html/js
COPY ./img /usr/share/nginx/html/img
COPY ./scss /usr/share/nginx/html/scss
COPY ./vendor /usr/share/nginx/html/vendor