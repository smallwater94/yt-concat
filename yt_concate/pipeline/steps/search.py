from yt_concate.pipeline.steps.step import Step


class Search(Step):
    def process(self, transporter, inputs, utils):
        counter = 0
        for yto in transporter:
            n = 0
            while True:
                try:
                    if inputs['search_word'] in yto.captions[n]['text']:
                        yto.time = yto.captions[n]['start']
                        yto.download_or_not = True
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
        return transporter
