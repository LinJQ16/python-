import requests
import os
from bs4 import BeautifulSoup as bs
url="https://bing.ioliu.cn/?p="
root="E://pics//"


if __name__=="__main__":
    if not os.path.exists(root):
        os.mkdir(root)
        
    for i in range(1,50):
        print('第'+str(i)+'页')
        content=requests.get(url+str(i))
        soup=bs(content.text,'html.parser')
        for div in soup.find_all('div', attrs={"class": "card progressive"}):
            downloadurl="https://bing.ioliu.cn/"+div.find('a',attrs={"class": "ctrl download"}).attrs['href']
            pic=requests.get(downloadurl,timeout=30)
            title=div.find('h3').string
            path=root+title.split(' (©')[0]+'.jpg'
            try:
                if not os.path.exists(path):
                    with open(path,'wb') as f:
                        f.write(pic.content)
                        f.close()
            except:
                print("保存失败")
                continue
