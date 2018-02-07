# sudo apt-get install mysql-client
# sudo apt-get install python-mysqldb
# sudo apt-get install python3-mysqldb

sudo /etc/init.d/mysql start

mysql -uroot --password -e "create database testKir;"

mysql -uroot --password -e "CREATE USER 'kirill'@'localhost' IDENTIFIED BY 'passwordKirill';"


# CREATE USER 'kirill'@'localhost' IDENTIFIED BY 'passwordKirill';

mysql -uroot --password -e "GRANT ALL ON testKir.* TO 'kirill'@'localhost';"
# GRANT ALL ON testKir.* TO 'kirill'@'localhost';

mysql -ukirill --password=passwordKirill -e "SHOW TABLES IN testKir;"

#mysql -ukirill --password=passwordKirill -e "SELECT * FROM testKir.questions_likes;"
#mysql -ukirill --password=passwordKirill -e "SELECT * FROM testKir.questions_likes INTO OUTFILE 'questions_likes.txt';"
#cat questions_likes.txt

#SHOW TABLES IN testKir;


#sudo apt-get install python3-mysqldb

cd /home/box/web/ask

python3 manage.py makemigrations

python3 manage.py migrate

# python3 -c "import django; print(django.get_version())"