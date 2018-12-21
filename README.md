# flask_linkedin

Let me start by saying that scraping linkedin is no easy task. It's like they went to court or something over this. ;)

This thing needs a lot of things, but it works, and pulls images. 

The hardest thing with scraping linked in is that they use dynamic elements for almost everything. Obviously, it is on
purpose. 

With that, it works... ok. The API? Great. The scraper... I'd rebuild it another way, mostly generating the data prior 
to the request. However, I wanted to show a triggering of events. 

That said, here is how this works.



Setup
- [x] python3.5 with Ubuntu 16.04LTS
- [x] set up virtual env

```$ pip3.5 install -r requirements.txt

```

Building out flask is as follows:

- [x] sudo apt-get update && sudo apt-get upgrade
- [x] sudo apt-get install apache2 
- [x] sudo apt-get update
- [x] sudo apt-get install apache2 apache2-dev
- [x] pip3.5 install mod_wsgi
- [x] mod_wsgi-express module-config
- [x] cp contents to nano /etc/apache2/mods-available/wsgi.load
- [x] a2enmod wsgi
- [x] service apache2 restart
- [x] pip3.5 install Flask
- [x] nano /etc/apache2/sites-available/FlaskApp.conf
- [x] update the ip to localhost (for now)

```
<VirtualHost *:80>
                ServerName 192.168.0.1
                ServerAdmin youremail@email.com
                WSGIScriptAlias / /var/www/FlaskApp/FlaskApp.wsgi
                <Directory /var/www/FlaskApp/FlaskApp/>
                        Order allow,deny
                        Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/FlaskApp-error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/FlaskApp-access.log combined
</VirtualHost>
```
- [x] sudo a2ensite FlaskApp
- [x] service apache2 reload

Boom, Now you can run the app.py application. To do so, go


```
$ python3.5 app.py
```
In another terminal, you'll need to run li_requestor.py, this will make the curl request.

```
$ python3.5 li_requestor.py 'name of company'
```

TBH, this thing is a bit of a hack, as you need to use li_requestor to replace whitespaces with "-". That happens 
under the urllify()

So, it is what it is, and I am proud that I even got it to work that much.
