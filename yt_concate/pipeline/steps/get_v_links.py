# urllib.error.HTTPError: HTTP Error 400: Bad Request 表示 CHANNEL_ID 或是 API_KEY 出問題。
# 也可能單純系統在搞你。


import urllib.request
import json

from yt_concate.settings import API_KEY
from yt_concate.pipeline.steps.step import Step


class GetVideoList(Step):
    def process(self, transporter, inputs):
        channel_id = inputs['channel_id']
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)  # fot test
        return video_links
