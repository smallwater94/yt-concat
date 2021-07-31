from __future__ import unicode_literals
import youtube_dl
import os
from yt_concate.pipeline.steps.step import Step


class DownLoadVideos(Step):

    def process(self, transporter, inputs, utils):
        counter = 0
        for yto in transporter:
            if yto.download_or_not is True and counter < 3:
                print('第', counter + 1, '支影片下載開始')
                save_path = '/'.join(os.getcwd().split('/')[:3]) + '/downloads/videos'
                file_name = f'/{yto.v_id}.mp4'

                # yortube_id operations，yortube_id的各項屬性，可以根據你的需求加減
                ydl_opts = {
                    'format': 'worst',  # 畫質：最差 (為預防我的C槽炸裂)
                    'outtmpl': save_path + file_name,  # 輸出模板：裝著路徑以及檔名
                }

                # 記得YoutubeDL()裡面裝著ydl_opt 以及download([url]) 是小誇號裝著中誇號
                youtube_dl.YoutubeDL(ydl_opts).download([yto.url])
                counter += 1
        print('影片下載完成')
