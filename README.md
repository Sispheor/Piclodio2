Piclodio2
=========

Piclodio2 is a web radio player and a also an alarm clock. You can add url stream to complete the collection. Scheduling alarm clock is easy and can be periodic.

![alt tag](https://raw.github.com/Sispheor/Piclodio2/master/img/piclodio_home.png)

Prerequisites
==========

Django Framework

```
sudo pip install Django==1.7.1
```

or download the last tarball from the offical website and then install it

```
tar xzf Django-1.7.1.tar.gz
sudo python setup.py install
```

mplayer, at and SQLite database
```
sudo apt-get install mplayer at sqlite3
```

Option 1 : use django's server to run piclodio
==========

It's not the best practice but it's easy and fast.

As pi user :

Get Piclodio
```
cd /home/pi
git clone https://github.com/Sispheor/Piclodio2.git
```
Copy the init script
```
sudo cp Piclodio2/init_script/piclodio.sh /etc/init.d/piclodio
sudo chmod +x /etc/init.d/piclodio
sudo update-rc.d piclodio defaults
```
You can edit it to customise settings
Start piclodio :
```
sudo /etc/init.d/piclodio start
```
That's it, you can now access your piclodio at http://youip:8000


Option 2 : run piclodio with apache
==========

Prerequisites
```
sudo apt-get install apache2 libapache2-mod-wsgi
```

Clone Piclodio application from github into apache document root directory
```
cd /var/www
git clone https://github.com/Sispheor/Piclodio2.git
```

Copy vHost from sources folder into apache vHost configuration folder
```
cp /var/www/Piclodio2/apache.piclodio.conf /etc/apache2/sites-available/
```

Enable the vHost
```
a2ensite piclodio
```
And last, we have to allow the Apache user www-data to use mplayer. Edit the sudoers file with the command
```
sudo visudo
```
and add this line at the end of the file
```
www-data ALL=NOPASSWD:/usr/bin/mplayer* ,/usr/bin/pgrep mplayer ,/usr/bin/killall mplayer, /usr/bin/at
```

That's it! Piclodio is now available on it IP adresse.

==========
