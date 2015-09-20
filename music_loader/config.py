__author__ = 'alexey'

import os


class Config(object):
    current_work_dir = os.getcwd()
    path_to_log = os.path.join(current_work_dir, "app.log")

    path_to_music = os.path.join(current_work_dir, "music")

    access_token = None
    redirect_uri = "https://oauth.vk.com/blank.html"
    scope="audio,offline"
    app_id = 5073036
    user_id = 159846879