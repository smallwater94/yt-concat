# pipeline 生產線
# 裝載著所有步驟
from yt_concate.pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        for work in self.steps:
            try:
                work.process(inputs)
            except StepException as err:
                print('休士頓，我們發現了一個錯誤！', err)
                break
