import requests
import json


def main():
    artist = "michel jackson" #input("artist name: ")
    data = get_data(artist)
    lister(data)




def get_data(artist):
    data = requests.get("https://itunes.apple.com/search?entity=song&limit=2000&term=" + artist ).json()
    
    return data


def lister(data):
    names = data["results"]
    for track in names:
        print(track["trackName"])
    










main()


