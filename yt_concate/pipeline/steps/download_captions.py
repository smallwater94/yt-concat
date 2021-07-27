# 下載字幕
from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step, StepException


class DownloadCaptions(Step):
    def process(self, transporter, inputs):

        for furl in transporter:
            try:
                url = self.get_video_id_from_url(furl)  # 擷取影片網址代號的部分

                # 使用 set 變量和 .get_transcript() 函數獲得的字典列表
                srt = YouTubeTranscriptApi.get_transcript(url)
            except:
                print('非英文或無字幕，網址: ', furl)
                continue

            with open(self.get_video_id_from_url(url) + '.txt', "w") as f:
                for i in srt:
                    f.write("{}\n".format(i))

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]
