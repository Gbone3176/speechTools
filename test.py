import os
from pocketsphinx import LiveSpeech, get_model_path, Decoder, Config

# 获取 PocketSphinx 模型路径
model_path = os.path.join(get_model_path(), "zh-cn")

# 设置解码器参数
config = Config()
config.set_string('-hmm', os.path.join(model_path, 'zh_cn.cd_cont_5000'))  # 中文声学模型路径
config.set_string('-lm', os.path.join(model_path, 'zh_cn.lm.bin'))        # 中文语言模型路径
config.set_string('-dict', os.path.join(model_path, 'zh_cn.dic'))         # 中文词典路径

# 初始化解码器
try:
    decoder = Decoder(config)
except RuntimeError as e:
    print(f"Decoder 初始化失败: {e}")
    exit(1)

# 检查音频文件格式是否为 PCM WAV (16kHz, 16位, 单声道)
audio_file = 'input/speechFiles/ailab_task.wav'
if not os.path.exists(audio_file):
    raise FileNotFoundError(f"音频文件不存在: {audio_file}")

# 读取音频文件并识别
with open(audio_file, 'rb') as f:
    decoder.start_utt()
    while True:
        buf = f.read(1024)
        if not buf:
            break
        decoder.process_raw(buf, False, False)
    decoder.end_utt()

# 获取识别结果
if decoder.hyp() is not None:
    print('识别结果: ', decoder.hyp().hypstr)
else:
    print('未识别到语音内容，请检查输入音频文件。')
