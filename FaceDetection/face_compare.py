import json
import os

from playsound import playsound

import face_compare_python3_demo


# 播放mp3
def play_sound(path: str):
    playsound(path)
    print('播放结束')
    # os.remove(path)


# 执行命令
def text_to_speech(text: str, file: str):
    print("edge-tts --text '{}' --write-media {} --voice zh-CN-YunxiNeural".format(text, file))
    os.system(
        'edge-tts --text "{}" --write-media {} --voice zh-CN-YunxiNeural'.format(text, file))


def face_compare(face_path:str) -> bool:
    with open('./users.json', "r") as f:
        people_data = json.loads(f.read())
    for key, value in people_data.items():
        print(face_path)
        print(value)
        is_true = face_compare_python3_demo.run(
            appid='',
            apisecret='',
            apikey='',
            img1_path=face_path,
            img2_path=value,
        )
        if is_true:
            # print("你好{}".format(key))
            # if key == 'person2':
            #     sound_path = './person2.mp3'
            # elif key == 'person1':
            #     sound_path = './person1.mp3'
            # else:
            #     pass
            sound_path = './{}.mp3'.format(key)
		        #  return  False
            #text_to_speech('检测到' + key, sound_path)
            play_sound(sound_path)
            return True
    return False
