# twitter_data_scrapping
Api para crear una base de datos a partir del feed de twitter

Esta api se conecta a tu cuenta de twitter y descarga los tweets que se encuentren en tu feed, además de los nombres de usuarios que los postean, y la fecha y hora de posteo.
A partir de estos datos crea un documento csv que los contiene.

Para utilizar la api, primero es necesario tener ciertas claves de seguridad de twitter: api key, api key secret, access token y access token secret.
Para obtener estas claves hace falta registrarse como developer en twitter: https://developer.twitter.com/. ¡Guarda muy bien estas claves!

Una vez que tengas las claves y tokens, ingresalos en el archivo conig.ini, de manera correspondiente y respectiva con cada variable (api_key = tu api key, etc).

Para que el programa funcione, es necesario instalar pandas, tweepy y configparser.
Al correr el archivo twitter_api.py se generará tu documento csv. 

Estoy trabajando en crear una versión ejecutable del código, y espero agregarla al repositorio próximamente.
