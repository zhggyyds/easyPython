from plotly import offline
from function import get_response_dict


url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
# 指定api版本
headers = {'Accept':'application/vnd.github.v7+json'}
# 将获取的json文件转换为字典
response_dict = get_response_dict(url, headers)
# 提取所有项目的具体信息
repo_dicts = response_dict['items']
links, stars, labels = [], [], []

# items值是一个嵌套着多个字典的列表，每个字典包括一个项目的所有信息
for dict in repo_dicts:
    name = dict['name']
    url = dict['html_url']
    link = f"<a href='{url}'>{name}</a>"
    links.append(link)
    stars.append(dict['stargazers_count'])

    owner = dict['owner']['login']
    description = dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type':'bar',
    'x':links,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60, 100, 150)',
        'line':{'width':1.5, 'color': 'rgb(25, 25 ,25)'}
    },
    'opacity':0.6,
}]

my_layout = {
    'title':'github上最受欢迎的C项目',
    'titlefont':{'size':28},
    'xaxis':{
        'title':'repository',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
        },
    'yaxis':{
        'title':'Stars',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
        },
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig)