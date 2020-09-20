import json
import folium 
import pandas as pd
import io
import csv
import branca # to put html into popups
import spotipy 
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import os
from folium.plugins import MarkerCluster
from folium.plugins import FloatImage

conf_file = os.path.join(os.path.dirname(__file__), '/conf.py')
exec(open(conf_file).read())



MIN_FOLLOWERS = 1000


mc = MarkerCluster()

def address_venu(venu_add):
    artists_code = "<ul>"
    artists_code += """<li><a>{address}</a></li>""".format(
        address=venu_add['address']+' '+venu_add['city']+' '+venu_add['country']
        )
    artists_code += "</ul>"
    return artists_code


def artists_to_html_list(spotipy_conn, artists_dict, artists_venue):
    artists_code = "<ul>"
    for perf in artists_dict:
        artists_code += """<li>
        <a title="Open on spotify" href={url_artist}>{name2}</a><br>
        <br><img class="fit-picture"
        src="{image_url}" width="300"></li><br>""".format(
            name2=perf['name'],
            image_url=perf['image'], 
            url_artist= perf['url']  
        )

        artist_spotify_id = get_spotify_id_from_name(spotipy_conn, perf['name'])
        if artist_spotify_id is not None:
            artists_code += """<iframe src="https://open.spotify.com/embed/artist/{artist_spotify_id}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
        </li><br>""".format(
            artist_spotify_id=artist_spotify_id
        )

        artists_code += "</li><br>"

    artists_code += "</ul>"
    return artists_code

def get_spotify_id_from_name(spotipy_conn, name):
    results = spotipy_conn.search(q=name, type='artist', limit=5)
    for artist in results['artists']['items']:
        if artist['followers']['total'] > MIN_FOLLOWERS:
            # Use this artists
            return artist['id']

def main(): 
    # Init map
    m = folium.Map(
        location=[36, -115],
        zoom_start=4,
        tiles='Stamen Terrain'
    )
    rock = folium.FeatureGroup(name='rock')
    m.add_child(rock)
    
    autre = folium.FeatureGroup(name='autre')
    m.add_child(autre) 
    
    # other mapping code (e.g. lines, markers etc.)
    

    #Init a base html structure
    html_template = """
        <h1>{vn}</h1><br>
        <h3>Adresse :</h3> {ad}
        <h3>Artists :</h3>
        {ac}
        </p>
    """

    # Open events json
    filename = os.path.join(os.path.dirname(__file__), '/samples/seetgeek_concert_event300.json')
    with open(filename, 'r') as f:
        distros_dict = json.load(f)

    # Init spotipy API
    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET
        )
    )

    tooltip = 'Click me!'
    for event in distros_dict['events']:
        lat = event['venue']['location']['lat']
        lon = event['venue']['location']['lon']
        venue_name = event['venue']['name']
        artists_code = artists_to_html_list(sp, event['performers'], event['venue'])
        venu_address=address_venu(event['venue'])
        iframe = branca.element.IFrame(html=html_template.format(vn=venue_name, ad=venu_address ,ac=artists_code), width=500, height=300)
        popup = folium.Popup(iframe, max_width=500)
        mc.add_child(folium.Marker([lat, lon], popup=popup, tooltip=tooltip,icon=folium.Icon(color='green', icon='info-sign'))).add_to(m)
    
    folium.TileLayer('OpenStreetMap').add_to(m)
    folium.LayerControl().add_to(m)
    m.save('output_map.html')



if __name__ == "__main__":
    main()

