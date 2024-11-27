import requests
import json
from configs import TOKEN

origin_record = "input/origin_record/origin_record.txt"
processed_record = "output/processed_record.md"
with open(origin_record, "r", encoding="utf-8") as file:
    meeting = file.read()  # 将文件内容读取为一个字符串

file_name = "output/Xqi_v1.md"
url = 'https://internlm-chat.intern-ai.org.cn/puyu/api/v1/chat/completions'
header = {
    'Content-Type':'application/json',
    "Authorization":"Bearer " + TOKEN
}
data = {
    "model": "internlm2.5-latest",
    "messages": [{
        "role": "user",
        "content": "这是一段会议记录，请为我将其总结成条理清晰的会议纪要：" + meeting
    }],
    "n": 1,
    "temperature": 0.8,
    "top_p": 0.9
}

res = requests.post(url, headers=header, data=json.dumps(data))
print("code: ", res.status_code)
data = res.json()
with open(processed_record, "w", encoding="utf-8") as file:
    file.write(data["choices"][0]["message"]["content"])

print(f"{processed_record} 文件已经创建并写入内容！")
