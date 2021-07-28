# utils 實用程式，屬於工具箱，裝著一些通用型小型def
import os
from yt_concate.settings import DOWNLOADS_DIR, CAPTIONS_DIR, VIDEOS_DIR
from yt_concate.model.yto import YTO


class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    # @staticmethod
    # def get_video_id_from_url(url):
    #     return url.split('watch?v=')[-1]

    def get_videos_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def videos_list_file_exists(self, channel_id):
        path = self.get_videos_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    # def get_caption_filepath(self, url):
    #     return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + '.txt')

    # def caption_file_exists(self):
    #     path = YTO.get_caption_filepath()
    #     return os.path.exists(path) and os.path.getsize(path) > 0
