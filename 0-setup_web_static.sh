#!/usr/bin/env bash
# Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

if [ ! -x /usr/sbin/nginx ];
then
    apt-get -y update
    apt-get -y install nginx
    ufw allow  'Nginx HTTP' #on port 80
    service nginx restart
else

    service nginx restart
fi
mkdir -p /data/web_static/releases/test
touch  /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.htm
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sudo sed -i "/listen 80 default_serve/a location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
