FROM nginx:alpine

COPY default.conf /etc/nginx/conf.d/default.conf

WORKDIR /var/www/html

COPY index.html /var/www/html

CMD ["nginx", "-g", "daemon off;"]