#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo update
sudo install -y nginx
# Start Nginx
sudo service nginx start

# Create an index.html file with "Hello World!"
echo "Hello World!" | sudo tee /var/www/html/index.html

# Configure redirection for /redirect_me
# shellcheck disable=SC1004

if grep -q "location /redirect_me" /etc/nginx/sites-available/default; then
	echo "skipping.. redirect_me exits"
else
	sudo sed -i '/server_name _;/a \
	\nlocation /redirect_me {\n\
	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n\
	}\n' /etc/nginx/sites-available/default
fi

# Create a custom 404 HTML page
sudo echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html

# Modify the Nginx configuration to use the custom 404 page
# shellcheck disable=SC1004

if grep -q "error_page 404 /custom_404.html" /etc/nginx/sites-available/default; then
        echo "skipping... custom 404 exist"
else
	sudo sed -i '/server_name _;/a \
	\nerror_page 404 /custom_404.html;\n\
	location /custom_404.html {\n\
	internal;\n\
	}\n' /etc/nginx/sites-available/default
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo 'fake html file' |sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

if grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
	echo "skipping...hbnb_static exitst"
else
	sudo sed -i '/server_name _;/a \
	\n\nlocation /hbnb_static {\n\
	alias /data/web_static/current/;\n\
	}\n' /etc/nginx/sites-available/default
fi

sudo service nginx restart