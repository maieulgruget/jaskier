
# Jaskier
Notre application cartographique se place dans ce contexte et cherche à répondre à ces 2 objectifs :
 - Pouvoir mettre de la musique sur une cartographie web
 - Pouvoir choisir un lieu de concert directement sur une carte

# Sources de données
Pour cela nous avons utilisé 2 sources de données :

## Seatgeek  
SeatGeek qui est une plateforme de billetterie mobile qui permet aux utilisateurs d’acheter et de vendre des billets pour des manifestations sportives, des concerts et des spectacles. Il a pour nous l’avantage d’avoir de la donnée de qualité facilement disponible à l’aide d’API bien documenté. Elle a l’inconvénient de vendre des billets uniquement aux États-Unis.

## Spotify  
Spotify est un service suédois de streaming musical sous la forme de logiciel propriétaire. Cette plateforme de musique permet une écoute quasi instantanée de fichier musical. Il propose des outils propices aux développements d’application musicale grâce à leurs plateformes web « Spotify for développer ». L’inconvénient de cette source est sa complexité pour pouvoir accéder aux outils proposé (authentification, hébergement de l’application, partage du script sur le serveur spotify…)

# Installation (Linux)
1. téléchargez ou clonez ce repository
2. placez-vous dans le répertoire du repository 
	  `cd jaskier`
3. Créez un environnement virtuel :
	 `sudo apt-get install python3-venv`
	 `python3 -m venv env`
4. Activez l'environnement virtuel
	 `source env/bin/activate`
5. Installez les modules pythons requis :
	 `pip install -r requirements.txt`
6. Récuper vos identifiants Spotify. Rendez vous sur [My Dashboard](https://developer.spotify.com/dashboard/applications) pour obtenir vos identifiants (un _client id_ et un _client secret_).
7. Dupliquez le fichier de configuration :
 `cp conf.py.sample conf.py`
8. Éditez ce fichier conf en y collant vos identifiants Spotify

# Usage
Exécutez le script python jaskier.py
`python3 jaskier.py`
Cela devrait générer une page html statique (output_map.py) contenant une carte. Cliquer sur chaque point fait apparaître une fiche présentant le concert et permettant d'écouter des morceaux de l'artiste via un module Spotify.

# Modules python utilisé  
Pour le développement de l’application, nous avons écrit le script en python sur VisualStudioCode et 3 bibliothèques sont à retenir :

## Follium
Follium est une bibliothèque python qui propose des outils cartographiques (création de cartes, points sur cartes, cluster…)

## Spotipy
Spotipy est une bibliothèque python qui simplifie l’accès aux outils spotify (widget dans notre cas) en facilitant l’authentification.

## Branca 
Branca permet la réalisation de popup HTML.

# Jaskier en démo vidéo  
Une vidéo présente l’application V1 et ses outils développés :
https://veillecarto2-0.fr/2020/04/08/jaskier-de-la-musique-sur-une-carte/

# Contexte
Le milieu de la musique a subi de plein fouet une croissance numérique dans les années 2000. Les ventes de produits matérielles (CD, cassettes, DVD) ont drastiquement chuté et les recettes pour les auteurs avec.

Il s’est finalement mieux adapté dans les années 2010. Les artistes se sont appropriés les réseaux sociaux pour communiquer directement avec leurs fans, la promotion s’est faite alors par ces vecteurs médiatiques (réseaux sociaux, articles, publicité web, plateforme musicale…)

Dans ce contexte, les concerts et festivals ont pris une part de plus en plus importante dans le monde de la musique et les recettes financières des artistes engendrées par ces « shows » ont remplacé la traditionnelle vente de CD.

La cartographie web n’a pas tellement percé comme outil de communication. Pourtant elle est un vecteur médiatique intéressant et pourrait apporter des informations pertinentes comme la localisation de concert et festivals à venir dans une zone géographique par exemple. Certaines applications comme Wycker, BandsInTown ou SongKick utilisent la cartographie comme support (localisation d’artistes, catégorisation de genre de musiques…), mais aucune n’a eu l’originalité encore de mettre de la musique sur une carte.

# Bibliographie

branca: Generate complex HTML+JS pages with Python (version 0.4.0). . https://github.com/python-visualization/branca.

« Console | Spotify for Developers ». https://developer.spotify.com/console/.

« Folium — Folium 0.10.1 documentation » https://python-visualization.github.io/folium/.

« LA CARTOGRAPHIE A L HEURE DU GEOWEB -. https://docplayer.fr/60055528-La-cartographie-a-l-heure-du-geoweb.html.

« SeatGeek Platform API Documentation ». https://platform.seatgeek.com/.

« Welcome to Spotipy! — spotipy 2.0 documentation ». https://spotipy.readthedocs.io/en/2.9.0/.

