sudo ln -s /home/box/WebTech18/web /home/box/web 

#sudo ln -s  etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/def*
sudo  ln -f  test_nginxDjango.cfg   /etc/nginx/sites-enabled/test.conf


#test_gunicornDjango.cfg 
#test_nginxDjango.cfg 

sudo  ln -f  test_gunicorn.cfg   /etc/gunicorn.d/test_gunicorn.cfg
sudo  ln -f  test_gunicornDjango.cfg   /etc/gunicorn.d/test_gunicornDjango.cfg


sudo /etc/init.d/nginx restart
#sudo systemctl status nginx.service

#gunicorn -w 4 hello:app
sudo /etc/init.d/gunicorn restart
#sudo systemctl status gunicorn.service

### TEST w/o service
# gunicorn --bind 0.0.0.0:8000 ask.wsgi

#sudo ln -s  etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start