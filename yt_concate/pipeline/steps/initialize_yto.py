from .step import Step
from yt_concate.model.yto import YTO


class InitializeYTO(Step):
    def process(self, transporter, inputs, utils):
        return [YTO(url) for url in transporter]
