sudo ln -s /home/box/WebTech18/web /home/box/web 

#sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/def*
sudo  ln -s /home/box/web/test_nginxDjango.cfg   /etc/nginx/sites-enabled/test.conf


#test_gunicornDjango.cfg 
#test_nginxDjango.cfg 

sudo  ln -s /home/box/web/test_gunicorn.cfg   /etc/gunicorn.d/test_gunicorn.cfg
sudo  ln -s /home/box/web/test_gunicornDjango.cfg   /etc/gunicorn.d/test_gunicornDjango.cfg


sudo /etc/init.d/nginx restart
sudo systemctl status nginx.service

#gunicorn -w 4 hello:app
sudo /etc/init.d/gunicorn restart
sudo systemctl status gunicorn.service


#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start