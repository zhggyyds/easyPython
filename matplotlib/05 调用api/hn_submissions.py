import requests
from operator import itemgetter
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# 此处获得一个包括所有热门文章id的列表
response_ids = r.json()
sub_dicts = []

for sub_id in response_ids[:8]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{sub_id}.json"
    r1 = requests.get(url)
    print(f"id: {sub_id} Status code: {r.status_code}")
    response_dict = r1.json()

    sub_dict = {
        'title':response_dict['title'],
        'hn_link':f"http://news.ycombinator.com/item?id={sub_id}",
        'comments':response_dict['descendants'],
    }
    sub_dicts.append(sub_dict)

sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)

links, comments = [], []
for sub_dict in sub_dicts:
    link = f"<a href='{sub_dict['hn_link']}'>{sub_dict['title']}</a>"
    links.append(link)
    comments.append(sub_dict['comments'])

data = [{
    'type':'bar',
    'x':links,
    'y':comments,
    'marker':{
        'color':'rgb(60, 100, 150)',
        'line':{'width':1.5, 'color': 'rgb(25, 25 ,25)'}
    },
    'opacity':0.6,
}]

my_layout = {
    'title':'hacker news 上最热门的文章',
    'titlefont':{'size':28},
    'xaxis':{
        'title':'title',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
        },
    'yaxis':{
        'title':'comments',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
        },
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig)