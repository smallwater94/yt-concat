from yt_concate.steps.get_v_links import GetVideoList
from yt_concate.steps.step import StepException

CHANNEL_ID = 'UCjXfkj5iapKHJrhYfAF9ZGg'

# 輸入字典
inputs = {
    'channel_id': CHANNEL_ID
}

# 步驟清單，裝著所有步驟，讓底下的for loop一個一個去call
steps = [
    GetVideoList(),
]


for work in steps:
    try:
        work.process(inputs)
    except StepException as err:
        print('休士頓，我們發現了一個錯誤！', err)
        break
