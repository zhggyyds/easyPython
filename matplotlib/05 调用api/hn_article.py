import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
# 获得一个字典
request_dic = r.json()

readable_file = '/Users/zhouhao/Desktop/本地仓库/Python/matplotlib/05 调用api/readable_data.json'
with open(readable_file,'w') as f:
    json.dump(request_dic, f, indent=4)