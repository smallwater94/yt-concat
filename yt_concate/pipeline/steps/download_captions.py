# 下載字幕

from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, transporter, inputs, utils):

        for furl in transporter:
            url = utils.get_video_id_from_url(furl)  # 擷取影片網址代號的部分
            if utils.caption_file_exists(url):
                print('已經下載過了喔:', url)
                continue
            try:
                # 使用 set 變量和 .get_transcript() 函數獲得的字典列表
                srt = YouTubeTranscriptApi.get_transcript(url)
            except:
                print('非英文或無字幕，網址: ', furl)
                continue
            print('寫入中', furl)
            with open(utils.get_caption_filepath(url), "w") as f:
                for i in srt:
                    f.write("{}\n".format(i))
