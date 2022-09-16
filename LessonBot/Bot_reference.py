import requests
from bs4 import BeautifulSoup

head={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'
}
r=requests.get('https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/',headers=head)
r.encoding = 'utf-8'

if(r.status_code)==200:
    print('Success')
    #print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)
    
    new_anime=soup.select_one('.timeline-ver > .newanime-block')
    anime_block=new_anime.select('.anime-block')
    for i in anime_block:
        anime_name=i.select_one('.anime-name >.anime-name_for-marquee').text.strip()
        print('動畫名: %s'%anime_name)
        try:
            anime_episode=i.select_one('.anime-episode > p').text.strip()
            print('目前級數: %s'%anime_episode)
        except:
            print('目前級數: 1')
        
        anime_watch=i.select_one('.anime-watch-number > p').text.strip()
        print('觀看人數: %s'%anime_watch)

        anime_herf=i.select_one('.anime-card-block').get('href')
        print('觀看連結 : https://ani.gamer.com.tw/%s'%anime_herf)

        print('')
else:
    print('Fail,status_code=%d'%r.status_code)

