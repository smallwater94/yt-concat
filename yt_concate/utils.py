# utils 實用程式，屬於工具箱，裝著一些通用型小型def
import os
from yt_concate.settings import CAPTION_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_path(self, url):
        return os.path.join(CAPTION_DIR, self.get_video_id_from_url(url) + '.txt')
