sudo ln -s /home/box/webtech18/web /home/box/web 

#sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo  ln -s /home/box/web/test.cfg  /etc/nginx/sites-enabled/test.conf


sudo /etc/init.d/nginx restart

#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start