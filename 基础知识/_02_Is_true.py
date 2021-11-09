# 对json文件的读写操作
import json
filename = 'user.json'


def greet_user(name):
    print(f"hello,{name}")


def get_new_username(name):
    with open(filename, 'w') as f:
        json.dump(name, f)


def is_exist():
    name = input("输入你的名字：")
    try:
        with open(filename) as f:
            content = json.load(f)
    except FileNotFoundError:
        return None
    else:
        if content != name:
            get_new_username(name)
            return name
        else:
            return content


def if_true():
    content = is_exist()
    if content:
        greet_user(content)
    else:
        get_new_username(content)
        greet_user(content)