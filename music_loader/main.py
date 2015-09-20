__author__ = 'alexey'

from config import Config
import logging
import urllib3
import json
import os

def save_token_into_config():
    args = (
        "client_id={}".format(Config.app_id),
        "display=page",
        "redirect_uri={}".format(Config.redirect_uri),
        "scope={}".format(Config.scope),
        "response_type=token",
        "v=5.37"
    )

    print("https://oauth.vk.com/authorize?" + "&".join(args))

    Config.access_token = input("Enter access_token: ")
    return Config.access_token


def get_list_sound_in_vk(httpd):
    res = httpd.urlopen("GET", "https://api.vk.com/method/audio.get?owner_id={}&access_token={}".format(
        Config.user_id, Config.access_token))
    return json.loads(res.data.decode())["response"][1:]


def save_into_disk(path, list, http):
    for sound in list:
        path_to_file = os.path.join(path, sound["title"] + ".mp3")
        if os.path.exists(path_to_file):
            continue

        with open(path_to_file, "wb") as file:
            file.write(http.urlopen("GET", sound["url"]).data)
        print(sound["title"] + " was downloaded!")

if __name__ == '__main__':
    logging.debug("init app")
    httpd = urllib3.PoolManager()
    access_token = save_token_into_config()
    save_into_disk(Config.path_to_music, get_list_sound_in_vk(httpd), httpd)