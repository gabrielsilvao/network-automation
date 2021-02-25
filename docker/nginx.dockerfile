FROM nginx:latest
MAINTAINER Gabriel
COPY /public /var/www/public
COPY /nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80 443
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]