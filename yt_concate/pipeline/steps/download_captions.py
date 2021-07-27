# 下載字幕
from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, transporter, inputs):
        for url in transporter:
            url = url.split('watch?v=')[-1]

            # 將字幕存進名為srt的字典
            # 通過 .get_transcript() 函數獲得
            srt = YouTubeTranscriptApi.get_transcript(url)

            for i in srt:
                print(i)

            break


