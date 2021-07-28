from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_v_links import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils

CHANNEL_ID = 'UCjXfkj5iapKHJrhYfAF9ZGg'

# 輸入字典
inputs = {
    'channel_id': CHANNEL_ID
}


def main():
    # 步驟清單，裝著所有步驟，讓底下的for loop一個一個去call
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
