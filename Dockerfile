FROM nginx:alpine
COPY ./index.html /usr/share/nginx/html/index.html
COPY .*.html /usr/share/nginx/html/