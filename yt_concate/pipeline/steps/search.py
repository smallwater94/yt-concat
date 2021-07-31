from yt_concate.pipeline.steps.step import Step
from yt_concate.model.catch_yto import CatchYTO

class Search(Step):
    def process(self, transporter, inputs, utils):
        found = []
        counter = 0
        for yto in transporter:
            n = 0
            while True:
                try:
                    if inputs['search_word'] in yto.captions[n]['text']:
                        time_start = yto.captions[n]['start']
                        time_duration = yto.captions[n]['duration']
                        c = CatchYTO(yto, time_start, time_duration)
                        found.append(c)
                        counter += 1
                        break
                except IndexError:
                    break
                except TypeError:
                    print('格式錯誤', yto.url)
                    break
                n += 1

        print('搜索任務完成')
        print('共找到', counter, '個影片有', inputs['search_word'])
        return found
