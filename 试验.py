import requests
from pyquery import PyQuery as pq
import os
headers={'referer': 'https://www.mzitu.com/'}


def index_get():
    url = 'https://www.mzitu.com/'
    response1 = requests.get(url)
    html = pq(response1.text)
    doc = html('#pins li span a').items()
    for i in doc:
        a_url = i.attr('href')
        title = i.text()
        a=page_parse(a_url)
        for a1 in a:
            img_download(a1,title)
            print('OK')

def page_parse(p_url):
    for i in range(1,11):
        curl=p_url+'/'+str(i)
        res=requests.get(curl)
        p_doc=pq(res.text)
        img_url=p_doc('.main-image img').attr.src
        yield img_url
        # next_url=p_doc('.pagenavi a:last-child').attr('href')




def img_download(img_url,title):
    img=requests.get(img_url,headers=headers)
    file_path = 'D:\wotian'
    file_name = title
    img_name=img_url[-10:-4]+'.jpg'
    file = file_path + '\\' + file_name + '\\'
    if not os.path.exists(file):
        os.makedirs(file)
    with open(file+img_name,'ab') as f:
        f.write(img.content)


index_get()

