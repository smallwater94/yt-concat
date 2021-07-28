# 下載字幕

from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, transporter, inputs, utils):

        for yto in transporter:
            if yto.caption_file_exists():
                print('已經下載過了喔:', yto.v_id)
                continue
            try:
                # 使用 set 變量和 .get_transcript() 函數獲得的字典列表
                srt = YouTubeTranscriptApi.get_transcript(yto.v_id)
            except:
                print('非英文或無字幕，網址: ', yto.url)
                continue
            print('寫入中', yto.url)
            with open(utils.get_caption_filepath(yto.v_id), "w") as f:
                for i in srt:
                    f.write("{}\n".format(i))
