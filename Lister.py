import requests
import cowsay
import json


def main():
    artist = input("artist name: ")
    num = input("how many songs you want to see ? :")
    data = get_data(artist , num)
    lister(data)


def get_data(artist , num):
    data = requests.get("https://itunes.apple.com/search?entity=song&limit="+ num + "&term=" + artist ).json()
    
    return data


def lister(data):
    names = data["results"]
    i = 1
    song = ""
    for track in names:
        if track["trackName"] not in song:
            song += (f"{i}  {track["trackName"]} ") + "\n"
            #
            i += 1

    
    cowsay.cow(song)

main()