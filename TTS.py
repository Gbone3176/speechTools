import speech_recognition as sr
from pydub import AudioSegment
import os

# 设定音频文件路径
audio_file = "input/speechFiles/ailab_task.mp3"  # 请将此更改为你的语音文件名
ori_record = os.path.join("input/origin_record", os.path.splitext(os.path.basename(audio_file))[0] + ".txt")

# 将 MP3 文件转换为 WAV 格式
audio = AudioSegment.from_mp3(audio_file)
wav_file_path = audio_file.rsplit(".", 1)[0] + ".wav"  # 确保获取正确的 WAV 文件路径
audio.export(wav_file_path, format="wav")

# 创建一个识别器实例
recognizer = sr.Recognizer()

# 使用 WAV 文件上下文管理器打开音频文件
with sr.AudioFile(wav_file_path) as source:  # 使用 WAV 文件而不是 MP3 文件
    # 记录文件中的音频
    audio_data = recognizer.record(source)  # 记录完整的音频数据

# 将音频转换为文本
try:
    text = recognizer.recognize_google(audio_data, language='zh-CN')  # 使用 Google Web Speech API
    with open(ori_record, "w") as text_file:
        text_file.write(text)
    print(f"文本转录结束，保存至{ori_record}")
except sr.UnknownValueError:
    print("抱歉，我无法识别音频")
except sr.RequestError:
    print("请求 Google Web Speech API 的服务器出错")
except ValueError as e:
    print(f"文件格式错误: {e}")  # 捕获并输出其他可能的异常