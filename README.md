# twitter_data_scrapping
This API can help you create a database from your Twitter feed

This API will connect to your Twitter account and download every tweet on your feed, with usernames and exact date of posting. Then it will create a CSV document with that data.

To use this API, first you need this Twitter security keys:api key, api key secret, access token and access token secret. To get this keys, you need to be registered as a Twitter developer: https://developer.twitter.com/. ¡Be sure to save those keys!

Once you have the keys, put them in the config.ini file.

To work correctly, the program needs to have pandas, tweepy and configparser installed. 
When you run the twitter_api.py file, the new csv file will be created.


# twitter_data_scrapping
Api para crear una base de datos a partir del feed de twitter

Esta api se conecta a tu cuenta de twitter y descarga los tweets que se encuentren en tu feed, además de los nombres de usuarios que los postean, y la fecha y hora de posteo.
A partir de estos datos crea un documento csv que los contiene.

Para utilizar la api, primero es necesario tener ciertas claves de seguridad de twitter: api key, api key secret, access token y access token secret.
Para obtener estas claves hace falta registrarse como developer en twitter: https://developer.twitter.com/. ¡Guarda muy bien estas claves!

Una vez que tengas las claves y tokens, ingresalos en el archivo conig.ini, de manera correspondiente y respectiva con cada variable (api_key = tu api key, etc).

Para que el programa funcione, es necesario instalar pandas, tweepy y configparser.
Al correr el archivo twitter_api.py se generará tu documento csv. 
