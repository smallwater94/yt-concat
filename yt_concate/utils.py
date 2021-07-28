# utils 實用程式，屬於工具箱，裝著一些通用型小型def
import os
from yt_concate.settings import DOWNLOADS_DIR, CAPTIONS_DIR, VIDEOS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    @staticmethod
    def get_video_id_from_url(furl):
        return furl.split('watch?v=')[-1]

    def get_caption_path(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + '.txt')
