# 下載字幕

from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, transporter, inputs, utils):

        for url in transporter:
            v_id = utils.get_video_id_from_url(url)  # 擷取影片網址代號的部分，當作video_id
            if utils.caption_file_exists(v_id):
                print('已經下載過了喔:', v_id)
                continue
            try:
                # 使用 set 變量和 .get_transcript() 函數獲得的字典列表
                srt = YouTubeTranscriptApi.get_transcript(v_id)
            except:
                print('非英文或無字幕，網址: ', url)
                continue
            print('寫入中', url)
            with open(utils.get_caption_filepath(v_id), "w") as f:
                for i in srt:
                    f.write("{}\n".format(i))
