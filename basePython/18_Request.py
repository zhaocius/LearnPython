import requests
import json

url = "http://10.199.0.63:9000/extract_with_detect"

payload = {}
files = [
  ('image', open('/Users/zhaozi/Documents/8.Files/TestPics/liudehua.jpg','rb'))
]
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

model=json.loads(response.text.encode('utf8'))
print(model.get('faces')[0].get('Feature'))
